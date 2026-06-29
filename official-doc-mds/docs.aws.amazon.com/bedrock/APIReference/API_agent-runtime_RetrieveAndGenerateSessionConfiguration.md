

# RetrieveAndGenerateSessionConfiguration
<a name="API_agent-runtime_RetrieveAndGenerateSessionConfiguration"></a>

Contains configuration about the session with the knowledge base.

This data type is used in the following API operations:
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) – in the `sessionConfiguration` field

## Contents
<a name="API_agent-runtime_RetrieveAndGenerateSessionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateSessionConfiguration-kmsKeyArn"></a>
The ARN of the AWS KMS key encrypting the session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: Yes

## See Also
<a name="API_agent-runtime_RetrieveAndGenerateSessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateSessionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateSessionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateSessionConfiguration) 