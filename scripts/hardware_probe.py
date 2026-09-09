import json, os, platform, shutil, subprocess


def run(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=10).strip()
    except Exception:
        return None

info = {
    'os': platform.platform(),
    'python': platform.python_version(),
    'cpu': platform.processor() or None,
    'ram_gb': None,
    'gpu_nvidia': None,
    'ffmpeg': shutil.which('ffmpeg'),
    'git': shutil.which('git')
}

try:
    if hasattr(os, 'sysconf'):
        pages = os.sysconf('SC_PHYS_PAGES')
        page_size = os.sysconf('SC_PAGE_SIZE')
        info['ram_gb'] = round((pages * page_size) / (1024**3), 1)
except Exception:
    pass

if shutil.which('nvidia-smi'):
    q = run(['nvidia-smi','--query-gpu=name,memory.total,driver_version','--format=csv,noheader'])
    info['gpu_nvidia'] = q

print(json.dumps(info, ensure_ascii=False, indent=2))
