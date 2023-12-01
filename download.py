import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import sys


def get_files_in_cid(cid):
    """Get a list of files within a given IPFS CID."""
    try:
        # Run the 'ipfs ls' command with the provided CID
        result = subprocess.run(
            ["ipfs", "ls", cid], capture_output=True, text=True, check=True
        )
        # Return the standard output
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Return the standard error if a CalledProcessError occurs
        return e.stderr


def extract_file_names(ipfs_ls_output):
    """Extract file names from the output of the 'ipfs ls' command."""
    file_names = []
    lines = ipfs_ls_output.strip().split("\n")

    for line in lines:
        file_name = line.split()[-1]
        file_names.append(file_name)
    return file_names


def call_executable(args):
    """Call an external executable with a list of arguments."""
    try:
        # Run the executable with the provided arguments
        result = subprocess.run(
            ['ipfs'] + args, capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Return the standard error if a CalledProcessError occurs
        return e.stderr


if __name__ == "__main__":

    if len(sys.argv) > 1:
        cid = sys.argv[1]
        print(f"CID: {cid}!")
        print("==========================================")
        print("Downloading files from the IPFS network...\n\n")
    else:
        print("Usage: python download.py <cid>\n")
        sys.exit(1)

    cid_path = os.path.join("downloads", cid)

    os.makedirs(cid_path, exist_ok=True)

    # List of arguments; each sublist is a set of arguments for one execution of the executable
    list_of_arguments = []

    files_list = extract_file_names(get_files_in_cid(cid))
    for file_name in files_list:
        list_of_arguments.append(
            [
                "get",
                os.path.join(cid, file_name),
                "-o",
                os.path.join(cid_path, file_name),
            ]
        )

    num_parallel_executions = os.cpu_count()

    # Using ThreadPoolExecutor to run the executable in parallel
    with ThreadPoolExecutor(max_workers=num_parallel_executions - 1) as executor:
        futures = [
            executor.submit(call_executable, args)
            for args in list_of_arguments
        ]

        for future in futures:
            print(future.result())
