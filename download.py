import os
import subprocess
from concurrent.futures import ThreadPoolExecutor


def call_executable(executable_path, args):
    """Call an external executable with a list of arguments."""
    try:
        print([executable_path] + args)
        # Run the executable with the provided arguments
        result = subprocess.run(
            [executable_path] + args, capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Return the standard error if a CalledProcessError occurs
        return e.stderr


if __name__ == "__main__":
    executable_path = "ipfs"

    cid = "QmQ2r6iMNpky5f1m4cnm3Yqw8VSvjuKpTcK1X7dBR1LkJF"
    cid_path = os.path.join('downloads', cid)

    os.makedirs(cid_path, exist_ok=True)

    # List of arguments; each sublist is a set of arguments for one execution of the executable
    list_of_arguments = [
        ["get", os.path.join(cid, "cat.gif"), '-o', os.path.join(cid_path, "cat.gif")],
    ]

    # Number of parallel executions
    num_parallel_executions = os.cpu_count()

    # Using ThreadPoolExecutor to run the executable in parallel
    with ThreadPoolExecutor(max_workers=num_parallel_executions - 1) as executor:
        futures = [
            executor.submit(call_executable, executable_path, args)
            for args in list_of_arguments
        ]

        for future in futures:
            print(future.result())
