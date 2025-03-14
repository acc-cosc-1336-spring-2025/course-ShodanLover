def get_hour(epoch_seconds):
    return (epoch_seconds // 3600) % 24

def get_minutes(epoch_seconds):
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):
    return epoch_seconds % 60

if __name__ == "__main__":
    test_value = 3800
    hours = get_hour(test_value)
    minutes = get_minutes(test_value)
    seconds = get_seconds(test_value)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
