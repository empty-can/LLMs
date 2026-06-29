

# MetadataAttributeValue
<a name="API_agent_MetadataAttributeValue"></a>

Contains the value of the metadata attribute. Choose a `type` and include the field that corresponds to it.

## Contents
<a name="API_agent_MetadataAttributeValue_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_MetadataAttributeValue-type"></a>
The type of the metadata attribute.  
Type: String  
Valid Values: `BOOLEAN | NUMBER | STRING | STRING_LIST`   
Required: Yes

 ** booleanValue **   <a name="bedrock-Type-agent_MetadataAttributeValue-booleanValue"></a>
The value of the Boolean metadata attribute.  
Type: Boolean  
Required: No

 ** numberValue **   <a name="bedrock-Type-agent_MetadataAttributeValue-numberValue"></a>
The value of the numeric metadata attribute.  
Type: Double  
Required: No

 ** stringListValue **   <a name="bedrock-Type-agent_MetadataAttributeValue-stringListValue"></a>
An array of strings that define the value of the metadata attribute.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** stringValue **   <a name="bedrock-Type-agent_MetadataAttributeValue-stringValue"></a>
The value of the string metadata attribute.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_agent_MetadataAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MetadataAttributeValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MetadataAttributeValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MetadataAttributeValue) 