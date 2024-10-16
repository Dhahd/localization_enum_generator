import re
import sys
import argparse

def camel_case(s):
    words = re.findall(r'[A-Za-z0-9]+', s)
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def generate_swift_enum(input_file, output_file):
    keys = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'"([^"]+)"\s*=', line)
            if match:
                keys.append(match.group(1))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("import Foundation\n\n")
        f.write("enum LocalizationKey: String {\n")
        for key in keys:
            f.write(f"    case {camel_case(key)} = \"{key}\"\n")
        f.write("}\n\n")
        f.write("func getString(_ key: LocalizationKey) -> String {\n")
        f.write("    return NSLocalizedString(key.rawValue, comment: \"\")\n")
        f.write("}\n")

def main():
    parser = argparse.ArgumentParser(description="Generate Swift enum from Localizable.strings file")
    parser.add_argument("input", help="Path to the input Localizable.strings file")
    parser.add_argument("output", help="Path to the output Swift file")
    
    args = parser.parse_args()

    generate_swift_enum(args.input, args.output)
    print(f"Generated {args.output} from {args.input}")

if __name__ == "__main__":
    main()