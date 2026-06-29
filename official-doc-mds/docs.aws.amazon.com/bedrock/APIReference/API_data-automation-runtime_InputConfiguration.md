

# InputConfiguration
<a name="API_data-automation-runtime_InputConfiguration"></a>

Input object settings for an invocation.

## Contents
<a name="API_data-automation-runtime_InputConfiguration_Contents"></a>

 ** s3Uri **   <a name="bedrock-Type-data-automation-runtime_InputConfiguration-s3Uri"></a>
The objects S3 URI.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/[^\x00-\x1F\x7F\{^}%`\]">\[~<#|]*)?`   
Required: Yes

 ** assetProcessingConfiguration **   <a name="bedrock-Type-data-automation-runtime_InputConfiguration-assetProcessingConfiguration"></a>
Lets you configure what portion of content you want to analyze. Works with passing segements of a larger video.  
Type: [AssetProcessingConfiguration](API_data-automation-runtime_AssetProcessingConfiguration.md) object  
Required: No

## See Also
<a name="API_data-automation-runtime_InputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/InputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/InputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/InputConfiguration) 