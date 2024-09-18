# Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

good_student = True if "Alice" in submitted and attended else False
print("Alice submitted their assignment and attended class" if good_student else 
      "Alice did not complete both of the prerequesites")
