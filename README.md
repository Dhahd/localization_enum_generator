# Localization Enum Generator for Swift

This Python script generates a Swift enum from a `Localizable.strings` file, making it easier to manage and use localized strings in your Swift projects.

## Features

- Converts `Localizable.strings` entries into a Swift enum
- Generates a helper function for easy string retrieval
- Supports custom input and output file paths
- Prevents typos and provides autocomplete for localization keys in your Swift code

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `localization_enum_generator.py` script.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script from the command line, providing the input `Localizable.strings` file path and the desired output Swift file path:

```
python localization_enum_generator.py <input_file_path> <output_file_path>
```

### Example

```
python localization_enum_generator.py ./Resources/Localizable.strings ./Sources/Generated/LocalizationKey.swift
```

## Output

The script generates a Swift file containing:

1. An enum `LocalizationKey` with cases for each localization key.
2. A `getString(_ key: LocalizationKey) -> String` function for easy string retrieval.

### Example Output

```swift
import Foundation

enum LocalizationKey: String {
    case appName = "app_name"
    case welcomeMessage = "welcome_message"
    // ... other cases
}

func getString(_ key: LocalizationKey) -> String {
    return NSLocalizedString(key.rawValue, comment: "")
}
```

## Integration with Xcode

1. Add a "Run Script" build phase to your target:
   - In Xcode, select your target
   - Go to "Build Phases"
   - Click the "+" button and choose "New Run Script Phase"
   - Add the following script:

   ```bash
   python "${SRCROOT}/path/to/localization_enum_generator.py" "${SRCROOT}/path/to/Localizable.strings" "${SRCROOT}/path/to/output/LocalizationKey.swift"
   ```

2. Adjust the paths in the script to match your project structure.
3. Make sure to add the output Swift file to your Xcode project if it's not already included.

Now, every time you build your project, the localization enum will be automatically updated if there are any changes in your `Localizable.strings` file.

## Usage in Swift Code

After generating the enum, you can use it in your Swift code like this:

```swift
let welcomeMessage = getString(.welcomeMessage)
```

This approach provides type safety and autocompletion for your localization keys.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
