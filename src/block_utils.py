# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list



from enum import Enum
import re

#Inline
class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered_list"
    ORDERED_LIST = "Ordered_list"


def block_to_block_type(block):
    # Heading: starts with 1-6 # characters, followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    # Code: starts and ends with 3 backticks
    if re.match(r"^```.*```$", block, re.DOTALL):
        return BlockType.CODE
    
    # Quote: every line starts with >
    if re.match(r"^(>.*(\n|$))+$", block):
        return BlockType.QUOTE
    
    # Unordered list: every line starts with - followed by a space
    if re.match(r"^(- .*(\n|$))+$", block):
        return BlockType.UNORDERED_LIST
    
    # Ordered list: lines start with sequential numbers (1., 2., etc)
    lines = block.split('\n')
    is_ordered = True
    for i, line in enumerate(lines, 1):
        if not re.match(f"^{i}\\. ", line):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    # Default: paragraph
    return BlockType.PARAGRAPH
