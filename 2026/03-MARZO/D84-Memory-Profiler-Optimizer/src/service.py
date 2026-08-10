class AnalyticsService:
    def __init__(self):
        self.memory_leak_cache = []

    def run_normal_process(self, size: int):
        """Procesa datos de forma temporal sin acumularlos permanentemente."""
        temp_data = [i * 2 for i in range(size)]
        return sum(temp_data)

    def run_leaky_process(self, size: int):
        """Simula una fuga de memoria acumulando datos en una lista interna."""
        leaky_data = [i * 3 for i in range(size)]
        self.memory_leak_cache.append(leaky_data)
        return len(self.memory_leak_cache)