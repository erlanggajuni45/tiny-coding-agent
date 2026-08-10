import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_abs_path, directory))
        valid_target_dir = os.path.commonpath([working_abs_path, target_dir]) == working_abs_path
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        contents_dir = os.listdir(target_dir)
        contents: list[str] = [] 
        for content in contents_dir:
            path = os.path.join(target_dir, content)
            contents.append(f'- {content}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}')

        return '\n'.join(contents)
    except Exception as e:
        return f'Error: {e}'