

# RequestMetadataBaseFilters
<a name="API_RequestMetadataBaseFilters"></a>

A mapping of a metadata key to a value that it should or should not equal.

## Contents
<a name="API_RequestMetadataBaseFilters_Contents"></a>

 ** equals **   <a name="bedrock-Type-RequestMetadataBaseFilters-equals"></a>
Include results where the key equals the value.  
Type: String to string map  
Map Entries: Maximum number of 1 item.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Key Pattern: `[a-zA-Z0-9\s._:/=+$@-]{1,256}`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+$@-]{0,256}`   
Required: No

 ** notEquals **   <a name="bedrock-Type-RequestMetadataBaseFilters-notEquals"></a>
Include results where the key does not equal the value.  
Type: String to string map  
Map Entries: Maximum number of 1 item.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Key Pattern: `[a-zA-Z0-9\s._:/=+$@-]{1,256}`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+$@-]{0,256}`   
Required: No

## See Also
<a name="API_RequestMetadataBaseFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RequestMetadataBaseFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RequestMetadataBaseFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RequestMetadataBaseFilters) 