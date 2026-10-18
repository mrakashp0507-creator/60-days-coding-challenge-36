
import time


def max_area_brute_force(heights):
    """Check every possible pair of walls."""
    n = len(heights)
    max_water = 0
    best_pair = (0, 0)

    for left in range(n):
        for right in range(left + 1, n):
            width = right - left
            water_height = min(heights[left], heights[right])
            area = width * water_height

            if area > max_water:
                max_water = area
                best_pair = (left, right)

    return max_water, best_pair


def max_area_two_pointers(heights):
    """Find maximum water capacity in linear time."""
    left = 0
    right = len(heights) - 1

    max_water = 0
    best_pair = (0, 0)

    while left < right:
        width = right - left
        water_height = min(heights[left], heights[right])
        area = width * water_height

        if area > max_water:
            max_water = area
            best_pair = (left, right)

        # Move the shorter wall inward.
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water, best_pair


def visualize_pointer_movement(heights):
    """Print each pointer movement and the calculated area."""
    left = 0
    right = len(heights) - 1
    max_water = 0
    step = 1

    print("\n=== TWO-POINTER VISUALIZATION ===")

    while left < right:
        width = right - left
        water_height = min(heights[left], heights[right])
        area = width * water_height

        max_water = max(max_water, area)

        print(f"\nStep {step}")
        print(f"  Left  : index {left}, height {heights[left]}")
        print(f"  Right : index {right}, height {heights[right]}")
        print(f"  Width : {width}")
        print(f"  Area  : {area}")
        print(f"  Best  : {max_water}")

        # Mark the walls currently being evaluated.
        visual = []
        for i, height in enumerate(heights):
            if i == left and i == right:
                visual.append(f"[{height}]")
            elif i == left:
                visual.append(f"L{height}")
            elif i == right:
                visual.append(f"R{height}")
            else:
                visual.append(str(height))

        print("  Walls :", " ".join(visual))

        if heights[left] < heights[right]:
            print(f"  Move LEFT: {heights[left]} is shorter.")
            left += 1
        elif heights[right] < heights[left]:
            print(f"  Move RIGHT: {heights[right]} is shorter.")
            right -= 1
        else:
            print("  Equal heights: move RIGHT.")
            right -= 1

        step += 1

    print("\nMaximum water capacity:", max_water)


def main():
    print("=" * 55)
    print("       FUTURISTIC RESERVOIR OPTIMIZER")
    print("=" * 55)

    raw_input = input(
        "Enter wall heights separated by spaces "
        "(e.g. 1 8 6 2 5 4 8 3 7): "
    )

    try:
        heights = list(map(int, raw_input.split()))

        if len(heights) < 2:
            print("Please enter at least two wall heights.")
            return

        if any(height < 0 for height in heights):
            print("Wall heights cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    # Brute-force benchmark
    start = time.perf_counter()
    brute_result, brute_pair = max_area_brute_force(heights)
    brute_time = time.perf_counter() - start

    # Optimized benchmark
    start = time.perf_counter()
    optimized_result, optimized_pair = max_area_two_pointers(heights)
    optimized_time = time.perf_counter() - start

    print("\n=== RESULTS ===")
    print("Wall heights:", heights)
    print(f"Brute-force maximum area: {brute_result}")
    print(f"Brute-force wall indices: {brute_pair}")
    print(f"Optimized maximum area:   {optimized_result}")
    print(f"Optimized wall indices:   {optimized_pair}")

    print("\n=== PERFORMANCE COMPARISON ===")
    print(f"Brute force:  {brute_time:.8f} seconds")
    print(f"Two pointers: {optimized_time:.8f} seconds")

    print("\nResults match:", brute_result == optimized_result)

    visualize_pointer_movement(heights)

    print("\n=== COMPLEXITY ===")
    print("Brute force:  O(n^2) time, O(1) auxiliary space")
    print("Two pointers: O(n) time,   O(1) auxiliary space")


if __name__ == "__main__":
    main()
