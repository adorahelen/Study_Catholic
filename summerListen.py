def calculate_pta(thresholds, method='three'):
    """
    Calculate the Pure Tone Average (PTA) using different methods.
    
    Args:
    thresholds (dict): Dictionary containing hearing thresholds with frequency in Hz as keys and threshold in dB as values.
                       Example: {500: 25, 1000: 30, 2000: 40, 4000: 35, 6000: 45, 8000: 50}
    method (str): The method to use for calculation ('three', 'four', 'six').
    
    Returns:
    float: The calculated PTA.
    """
    if method == 'three':
        frequencies = [500, 1000, 2000]
    elif method == 'four':
        frequencies = [500, 1000, 2000, 4000]
    elif method == 'six':
        frequencies = [250, 500, 1000, 2000, 4000, 8000]
    else:
        raise ValueError("Invalid method. Choose 'three', 'four', or 'six'.")
    
    total_threshold = 0
    count = 0
    
    for freq in frequencies:
        if freq in thresholds:
            total_threshold += thresholds[freq]
            count += 1
    
    if count == 0:
        raise ValueError("No thresholds provided for the specified frequencies.")
    
    pta = total_threshold / count
    return pta

# Function to get input from the user
def get_thresholds():
    """
    Get hearing thresholds for specified frequencies from user input.
    
    Returns:
    dict: Dictionary containing hearing thresholds with frequency in Hz as keys and threshold in dB as values.
    """
    frequencies = [125, 250, 500, 1000, 2000, 4000, 8000]
    thresholds = {}
    
    print("주파수(Hz)와 청력 역치(dB)를 입력하십시오.")
    for freq in frequencies:
        while True:
            try:
                threshold = float(input(f"{freq} Hz에 대한 청력 역치를 입력하십시오: "))
                thresholds[freq] = threshold
                break
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력하십시오.")
    
    return thresholds

# Example usage
thresholds = get_thresholds()

# Calculating PTA using different methods
pta_three = calculate_pta(thresholds, method='three')
pta_four = calculate_pta(thresholds, method='four')
pta_six = calculate_pta(thresholds, method='six')

print(f"3분법 PTA: {pta_three} dB")
print(f"4분법 PTA: {pta_four} dB")
print(f"6분법 PTA: {pta_six} dB")
