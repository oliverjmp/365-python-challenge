import subprocess
import sys
from typing import Tuple

class QualityGateEnforcer:
    """Validador estricto de calidad y umbral de cobertura de código."""
    def __init__(self, min_coverage_percentage: float = 100.0):
        self.min_coverage_percentage = min_coverage_percentage

    def check_coverage(self, source_dir: str = "src") -> Tuple[bool, str]:
        """Ejecuta pytest con coverage y valida si se cumple el umbral estricto."""
        cmd = [
            sys.executable, "-m", "pytest",
            f"--cov={source_dir}",
            f"--cov-fail-under={self.min_coverage_percentage}",
            "--quiet"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        passed = result.returncode == 0
        output_message = result.stdout if passed else result.stderr
        
        return passed, output_message