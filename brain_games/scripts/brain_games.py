#!/usr/bin/env python
import prompt


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May i have your name? ')
    print(f'Hello, {user_name}!')


if __name__ == '__main__':
    main()
