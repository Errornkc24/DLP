import re

# Define token types
TOKEN_TYPES = {
    'KEYWORD': r'\b(int|char|return|void|struct|long|float|if|else|for|while|do|break|continue|switch|case|default|sizeof|typedef|static|extern|const|volatile|goto|enum|union|register|inline|restrict)\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'CONSTANT': r'\b\d+\b',
    'STRING': r'\'[^\']*\'|"[^"]*"',  # Single and double quotes
    'PUNCTUATION': r'[{}()\[\];,]',
    'OPERATOR': r'[+\-*/=<>!&|]+',
}

def remove_comments(code):
    # Remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove single-line comments
    code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
    return code

def tokenize(code):
    # First remove all comments
    code = remove_comments(code)
    
    # Split the code into potential tokens including invalid ones
    tokens = []
    words = re.findall(r'[a-zA-Z_]\w*|[0-9]+[A-Za-z0-9]*|\S', code)
    
    for word in words:
        # Check for keywords
        if re.match(TOKEN_TYPES['KEYWORD'], word):
            tokens.append(('Keyword', word))
        # Check for valid identifiers
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word):
            tokens.append(('Identifier', word))
        # Check for valid constants
        elif re.match(r'^\d+$', word):
            tokens.append(('Constant', word))
        # Check for strings
        elif re.match(TOKEN_TYPES['STRING'], word):
            tokens.append(('String', word))
        # Check for punctuation
        elif re.match(TOKEN_TYPES['PUNCTUATION'], word):
            tokens.append(('Punctuation', word))
        # Check for operators
        elif re.match(TOKEN_TYPES['OPERATOR'], word):
            tokens.append(('Operator', word))
        # Invalid lexemes (like 7H)
        elif re.match(r'\d+[A-Za-z0-9]*', word):
            tokens.append(('Invalid', word))
        
    return tokens

def process_code(file_path):
    # Read the C code from the specified file
    with open(file_path, 'r') as file:
        c_code = file.read()
    
    tokens = tokenize(c_code)
    symbol_table = set()
    lexical_errors = []
    
    # Process tokens and build symbol table
    for token_type, token_value in tokens:
        if token_type == 'Identifier':
            symbol_table.add(token_value)
        elif token_type == 'Invalid':
            lexical_errors.append(f"{token_value} invalid lexeme")
    
    # Print results in the exact format required
    print("TOKENS")
    for token_type, token_value in tokens:
        if token_type != 'Invalid':  # Don't print invalid tokens in the token list
            print(f"{token_type}: {token_value}")
    
    if lexical_errors:
        print("\nLEXICAL ERRORS")
        for error in lexical_errors:
            print(error)
    
    print("\nSYMBOL TABLE ENTRIES")
    for idx, identifier in enumerate(sorted(symbol_table), start=1):
        print(f"{idx}) {identifier}")

# Example usage
file_path = "D:/Charusat University/Practicals/SEM-6/DLP/P3 c programs/test_code.c"  # Update this path to your C source file
process_code(file_path)