

# IndexedKey
<a name="API_IndexedKey"></a>

A metadata key indexed for filtering.

## Contents
<a name="API_IndexedKey_Contents"></a>

 ** key **   <a name="bedrockagentcorecontrol-Type-IndexedKey-key"></a>
The metadata key name to index.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

 ** type **   <a name="bedrockagentcorecontrol-Type-IndexedKey-type"></a>
The data type of the indexed key.  
Type: String  
Valid Values: `STRING | STRINGLIST | NUMBER`   
Required: Yes

## See Also
<a name="API_IndexedKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/IndexedKey) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/IndexedKey) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/IndexedKey) 