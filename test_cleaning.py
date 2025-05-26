#!/usr/bin/env python3
"""Simple test script to verify text cleaning functionality"""

from clipclean.cleaner import LLMTextCleaner

def test_cleaning():
    cleaner = LLMTextCleaner()
    
    # Test cases with common LLM output issues
    test_cases = [
        # Smart quotes
        ('He said "Hello World" today', 'He said "Hello World" today'),
        
        # Special dashes
        ("AI – the future of technology", "AI - the future of technology"),
        
        # Non-breaking spaces
        ("Hello\xa0World", "Hello World"),
        
        # Multiple issues
        ('"AI is amazing," she said – truly revolutionary…', '"AI is amazing," she said - truly revolutionary...'),
        
        # Excessive whitespace
        ("Hello    World\n\n\n\nNext paragraph", "Hello World\n\nNext paragraph"),
        
        # Zero-width characters
        ("Hello\u200bWorld\ufeff", "HelloWorld"),
    ]
    
    print("Testing ClipClean text cleaning:")
    print("=" * 50)
    
    for i, (input_text, expected) in enumerate(test_cases, 1):
        result = cleaner.clean(input_text)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i}: {status}")
        print(f"  Input:    {repr(input_text)}")
        print(f"  Expected: {repr(expected)}")
        print(f"  Got:      {repr(result)}")
        print()

if __name__ == "__main__":
    test_cleaning()