import psutil
import logging

class OSProcessManager:
    def __init__(self, cpu_threshold: float = 80.0, mem_threshold: float = 80.0):
        self.cpu_threshold = cpu_threshold
        self.mem_threshold = mem_threshold

    def list_running_processes(self) -> list:
        """Devuelve una lista de diccionarios con información básica de los procesos activos."""
        process_list = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                process_list.append({
                    "pid": pinfo.get("pid"),
                    "name": pinfo.get("name"),
                    "cpu_percent": pinfo.get("cpu_percent") or 0.0,
                    "memory_percent": pinfo.get("memory_percent") or 0.0
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return process_list

    def check_and_terminate_heavy_processes(self) -> list:
        """Monitorea los procesos y termina aquellos que superen los umbrales configurados."""
        terminated = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                pid = pinfo.get("pid")
                name = pinfo.get("name")
                cpu = pinfo.get("cpu_percent") or 0.0
                mem = pinfo.get("memory_percent") or 0.0

                if cpu > self.cpu_threshold or mem > self.mem_threshold:
                    # Evitamos terminar procesos críticos del sistema operativo
                    if name and name.lower() in ["system", "idle", "registry", "csrss.exe", "wininit.exe"]:
                        continue
                    
                    p = psutil.Process(pid)
                    p.terminate()
                    terminated.append({"pid": pid, "name": name, "cpu": cpu, "memory": mem})
                    logging.warning(f"[!] Proceso terminado por alto consumo: PID {pid} ({name}) - CPU: {cpu}%, MEM: {mem}%")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return terminated