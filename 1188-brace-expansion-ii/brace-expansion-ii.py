class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        n = len(expression)
        i = 0

        def multiply(a, b):
            return {x + y for x in a for y in b}

        def parse_expr():
            nonlocal i

            result = parse_term()

            while i < n and expression[i] == ',':
                i += 1
                result |= parse_term()

            return result

        def parse_term():
            nonlocal i

            result = {""}

            while i < n and expression[i] not in "},":
                result = multiply(result, parse_factor())

            return result

        def parse_factor():
            nonlocal i

            if expression[i] == '{':
                i += 1
                result = parse_expr()
                i += 1
                return result

            ch = expression[i]
            i += 1
            return {ch}

        return sorted(parse_expr())