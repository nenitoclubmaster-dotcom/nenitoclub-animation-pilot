import json
import os
import platform
import shutil
import subprocess
import sys


def run(cmd):
    try:
        return subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, text=True, timeout=15
        ).strip()
    except Exception:
        return None


def powershell(script):
    exe = shutil.which('powershell') or shutil.which('pwsh')
    if not exe:
        return None
    return run([exe, '-NoProfile', '-Command', script])


def get_ram_gb():
    # Linux/macOS/Unix
    try:
        if hasattr(os, 'sysconf'):
            pages = os.sysconf('SC_PHYS_PAGES')
            page_size = os.sysconf('SC_PAGE_SIZE')
            if isinstance(pages, int) and isinstance(page_size, int):
                return round((pages * page_size) / (1024**3), 1)
    except Exception:
        pass

    # Windows
    out = powershell(
        "[math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB,1)"
    )
    if out:
        try:
            return float(out.splitlines()[-1].replace(',', '.'))
        except Exception:
            pass
    return None


def get_cpu():
    cpu = platform.processor().strip()
    if cpu:
        return cpu
    out = powershell("(Get-CimInstance Win32_Processor | Select-Object -First 1 -ExpandProperty Name)")
    if out:
        return out.strip()
    return None


def get_gpu_info():
    data = {'nvidia': None, 'windows_video_controllers': None}
    if shutil.which('nvidia-smi'):
        data['nvidia'] = run([
            'nvidia-smi',
            '--query-gpu=name,memory.total,driver_version',
            '--format=csv,noheader'
        ])

    if platform.system().lower() == 'windows':
        out = powershell(
            "Get-CimInstance Win32_VideoController | "
            "Select-Object Name,AdapterRAM,DriverVersion | ConvertTo-Json -Compress"
        )
        data['windows_video_controllers'] = out
    return data


def get_torch_info():
    try:
        import torch
        return {
            'installed': True,
            'version': torch.__version__,
            'cuda_available': bool(torch.cuda.is_available()),
            'cuda_version': torch.version.cuda,
            'device_count': torch.cuda.device_count() if torch.cuda.is_available() else 0,
            'device_names': [
                torch.cuda.get_device_name(i)
                for i in range(torch.cuda.device_count())
            ] if torch.cuda.is_available() else []
        }
    except Exception:
        return {'installed': False}


def get_disk_free_gb(path=None):
    try:
        target = path or os.getcwd()
        total, used, free = shutil.disk_usage(target)
        return {
            'path': os.path.abspath(target),
            'free_gb': round(free / (1024**3), 1),
            'total_gb': round(total / (1024**3), 1)
        }
    except Exception:
        return None


info = {
    'os': platform.platform(),
    'system': platform.system(),
    'machine': platform.machine(),
    'python': platform.python_version(),
    'python_executable': sys.executable,
    'cpu': get_cpu(),
    'logical_cpu_count': os.cpu_count(),
    'ram_gb': get_ram_gb(),
    'gpu': get_gpu_info(),
    'torch': get_torch_info(),
    'disk': get_disk_free_gb(),
    'tools': {
        'ffmpeg': shutil.which('ffmpeg'),
        'git': shutil.which('git'),
        'nvidia_smi': shutil.which('nvidia-smi')
    }
}

print(json.dumps(info, ensure_ascii=False, indent=2))
