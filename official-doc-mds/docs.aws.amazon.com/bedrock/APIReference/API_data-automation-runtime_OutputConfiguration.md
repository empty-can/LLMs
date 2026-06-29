

# OutputConfiguration
<a name="API_data-automation-runtime_OutputConfiguration"></a>

Output settings for an invocation. The service adds a unique invocation ID to the path that you specify and stores output objects under that path.

## Contents
<a name="API_data-automation-runtime_OutputConfiguration_Contents"></a>

 ** s3Uri **   <a name="bedrock-Type-data-automation-runtime_OutputConfiguration-s3Uri"></a>
The S3 URI for invocation output.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/[^\x00-\x1F\x7F\{^}%`\]">\[~<#|]*)?`   
Required: Yes

## See Also
<a name="API_data-automation-runtime_OutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/OutputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/OutputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/OutputConfiguration) 