import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_abs_path, file_path))
        valid_target_dir = os.path.commonpath([working_abs_path, target_file]) == working_abs_path
                
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
            
        if not file_path.lower().endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args is not None:
            command.extend(args)
            
        result = subprocess.run(command, text=True, timeout=30, capture_output=True)
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        if result.stdout == '' and result.stderr == '':
            return 'No output produced'
        
        return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"