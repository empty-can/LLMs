

# RequestMetadataFilters
<a name="API_RequestMetadataFilters"></a>

Rules for filtering invocation logs. A filter can be a mapping of a metadata key to a value that it should or should not equal (a base filter), or a list of base filters that are all applied with `AND` or `OR` logical operators

## Contents
<a name="API_RequestMetadataFilters_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andAll **   <a name="bedrock-Type-RequestMetadataFilters-andAll"></a>
Include results where all of the based filters match.  
Type: Array of [RequestMetadataBaseFilters](API_RequestMetadataBaseFilters.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Required: No

 ** equals **   <a name="bedrock-Type-RequestMetadataFilters-equals"></a>
Include results where the key equals the value.  
Type: String to string map  
Map Entries: Maximum number of 1 item.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Key Pattern: `[a-zA-Z0-9\s._:/=+$@-]{1,256}`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+$@-]{0,256}`   
Required: No

 ** notEquals **   <a name="bedrock-Type-RequestMetadataFilters-notEquals"></a>
Include results where the key does not equal the value.  
Type: String to string map  
Map Entries: Maximum number of 1 item.  
Key Length Constraints: Minimum length of 1. Maximum length of 256.  
Key Pattern: `[a-zA-Z0-9\s._:/=+$@-]{1,256}`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+$@-]{0,256}`   
Required: No

 ** orAll **   <a name="bedrock-Type-RequestMetadataFilters-orAll"></a>
Include results where any of the base filters match.  
Type: Array of [RequestMetadataBaseFilters](API_RequestMetadataBaseFilters.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Required: No

## See Also
<a name="API_RequestMetadataFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RequestMetadataFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RequestMetadataFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RequestMetadataFilters) 