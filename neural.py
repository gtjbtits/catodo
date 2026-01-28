def print_color_bar(value, desc="Value", width=40):
    value = max(-10, min(10, value))
    position = int(((value + 10) / 20) * (width - 1))
    center = width // 2
    
    RED = "\033[91m"
    GREEN = "\033[92m"
    GRAY = "\033[90m"
    RESET = "\033[0m"
    
    bar = []
    for i in range(width):
        if i == center:
            bar.append(f"{GRAY}|{RESET}")
        elif value > 0 and center <= i <= position:
            bar.append(f"{GREEN}█{RESET}")
        elif value < 0 and position <= i <= center:
            bar.append(f"{RED}█{RESET}")
        elif i == position:
            if value > 0:
                bar.append(f"{GREEN}▶{RESET}")
            elif value < 0:
                bar.append(f"{RED}◀{RESET}")
            else:
                bar.append(f"{GRAY}|{RESET}")
        else:
            bar.append(" ")
    
    bar_str = "".join(bar)
    labels = f"-10{' ' * (center - 4)}0{' ' * (center - 4)}10"
    
    print(f"{bar_str} ({value:5.2f}) {desc}")
    # print(bar_str)
    # print(labels)
    
    return bar_str


def get_color_bar(value, width=40):
    value = max(-10, min(10, value))
    position = int(((value + 10) / 20) * (width - 1))
    center = width // 2
    
    RED = "\033[91m"
    GREEN = "\033[92m"
    GRAY = "\033[90m"
    RESET = "\033[0m"
    
    bar = []
    for i in range(width):
        if i == center:
            bar.append(f"{GRAY}|{RESET}")
        elif value > 0 and center <= i <= position:
            bar.append(f"{GREEN}█{RESET}")
        elif value < 0 and position <= i <= center:
            bar.append(f"{RED}█{RESET}")
        elif i == position:
            if value > 0:
                bar.append(f"{GREEN}▶{RESET}")
            elif value < 0:
                bar.append(f"{RED}◀{RESET}")
            else:
                bar.append(f"{GRAY}|{RESET}")
        else:
            bar.append(" ")
    
    bar_str = "".join(bar)
    labels = f"-10{' ' * (center - 4)}0{' ' * (center - 4)}10"
    
    return f"Value: {value:5.2f}\n{bar_str}\n{labels}"

if __name__ == "__main__":
    print_color_bar(-1, "Время")