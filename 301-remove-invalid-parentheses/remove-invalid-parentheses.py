class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        # BFS initialization
        queue = {s}
        visited = {s}
        
        while queue:
            # Check if any valid strings exist in the current level
            valid_results = [st for st in queue if is_valid(st)]
            if valid_results:
                return valid_results
            
            # Generate the next level by removing one parenthesis at a time
            next_level = set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in ('(', ')'):
                        # Remove character at index i
                        new_string = string[:i] + string[i+1:]
                        if new_string not in visited:
                            visited.add(new_string)
                            next_level.add(new_string)
            queue = next_level
        
        return [""]
