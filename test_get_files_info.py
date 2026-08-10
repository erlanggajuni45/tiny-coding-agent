from functions.get_files_info import get_files_info

list_to_check: list[str] = ['.', 'pkg', '/bin', '../']

for dir in list_to_check:
    print(f"Result for '{dir}' directory:")
    print(get_files_info('calculator', dir))
