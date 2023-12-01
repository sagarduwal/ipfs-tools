import sys

import subprocess


def get_files_in_cid(cid):
    """Get a list of files within a given IPFS CID."""
    try:
        result = subprocess.run(
            ["ipfs", "ls", cid], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr


def extract_file_names(ipfs_ls_output):
    file_names = []
    lines = ipfs_ls_output.strip().split("\n")
    for line in lines:
        file_name = line.split()[-1]
        file_names.append(file_name)

    return file_names


if __name__ == "__main__":    
    if len(sys.argv) > 1:
        cid = sys.argv[1]
    files_list = extract_file_names(get_files_in_cid(cid))
    print(files_list)
