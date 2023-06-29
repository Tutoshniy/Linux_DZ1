import subprocess
import string


def str_in_command(command, str, punct=False) -> str:
    result = command
    out = result.stdout
    lst = out.split('\n')
    if punct:
        lst = [''.join(c for c in s if c not in string.punctuation) for s in lst]
        print(lst)

    if str in out:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    print(str_in_command(subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8'),
                         'jammy', True))
    print(str_in_command(subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8'),
                         'jammy'))
