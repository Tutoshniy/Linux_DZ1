import subprocess


def str_in_command(command, string) -> str:
    result = command
    out = result.stdout
    print(out)

    if string in out:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    print(str_in_command(subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8'),
                         'denny'))
    print(str_in_command(subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8'),
                         'jammy'))
