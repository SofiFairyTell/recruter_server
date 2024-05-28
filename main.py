from ahp import ahp


def main():
    print("Analytic Hierarchy Process (AHP)")
    
    criteria = []
    comparisons = {}
    
    num_criteria = int(input("Enter the number of criteria: "))
    
    for i in range(num_criteria):
        criterion = input(f"Enter criterion {i + 1}: ")
        criteria.append(criterion)
    
    print("Enter the pairwise comparisons (i.e., 'criterion1 criterion2 value'):")
    print("For example, '1 2 3' means criterion 1 is 3 times more important than criterion 2.")
    
    for i in range(num_criteria):
        for j in range(i + 1, num_criteria):
            comparison = input(f"Enter comparison for {criteria[i]} vs {criteria[j]}: ")
            comparisons[(i, j)] = float(comparison)
    
    priority_vector, consistency_ratio = ahp(criteria, comparisons)
    
    print("\nPriority Vector:")
    for i, value in enumerate(priority_vector):
        print(f"{criteria[i]}: {value:.4f}")
    
    print(f"\nConsistency Ratio: {consistency_ratio:.4f}")
    if consistency_ratio > 0.1:
        print("Warning: The consistency ratio is greater than 0.1, indicating inconsistent judgments.")

if __name__ == "__main__":
    main()
