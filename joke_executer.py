from get_joke import get, text_map

def main():
    wrapped_joke = get()
    print(text_map(wrapped_joke))


if __name__ == "__main__":
    main()
