from get_joke import get, text_map

def main():
    wrapped_joke = get()
    print('Is its Joke with B category:\n')
    print(text_map(wrapped_joke))


if __name__ == "__main__":
    main()
