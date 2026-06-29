

# ImportedModelSummary
<a name="API_ImportedModelSummary"></a>

Information about the imported model.

## Contents
<a name="API_ImportedModelSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-ImportedModelSummary-creationTime"></a>
Creation time of the imported model.  
Type: Timestamp  
Required: Yes

 ** modelArn **   <a name="bedrock-Type-ImportedModelSummary-modelArn"></a>
The Amazon Resource Name (ARN) of the imported model.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:imported-model/[a-z0-9]{12}`   
Required: Yes

 ** modelName **   <a name="bedrock-Type-ImportedModelSummary-modelName"></a>
Name of the imported model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+`   
Required: Yes

 ** instructSupported **   <a name="bedrock-Type-ImportedModelSummary-instructSupported"></a>
Specifies if the imported model supports converse.  
Type: Boolean  
Required: No

 ** modelArchitecture **   <a name="bedrock-Type-ImportedModelSummary-modelArchitecture"></a>
The architecture of the imported model.  
Type: String  
Required: No

## See Also
<a name="API_ImportedModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ImportedModelSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ImportedModelSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ImportedModelSummary) 