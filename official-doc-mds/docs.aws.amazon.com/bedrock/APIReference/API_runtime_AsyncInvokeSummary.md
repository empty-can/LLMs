

# AsyncInvokeSummary
<a name="API_runtime_AsyncInvokeSummary"></a>

A summary of an asynchronous invocation.

## Contents
<a name="API_runtime_AsyncInvokeSummary_Contents"></a>

 ** invocationArn **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-invocationArn"></a>
The invocation's ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:async-invoke/[a-z0-9]{12}`   
Required: Yes

 ** modelArn **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-modelArn"></a>
The invoked model's ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:[a-z0-9\-]+:bedrock:[a-z0-9\-]*:[0-9]*:(provisioned-model|foundation-model)/.+`   
Required: Yes

 ** outputDataConfig **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-outputDataConfig"></a>
The invocation's output data settings.  
Type: [AsyncInvokeOutputDataConfig](API_runtime_AsyncInvokeOutputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** submitTime **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-submitTime"></a>
When the invocation was submitted.  
Type: Timestamp  
Required: Yes

 ** clientRequestToken **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-clientRequestToken"></a>
The invocation's idempotency token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[!-~]*`   
Required: No

 ** endTime **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-endTime"></a>
When the invocation ended.  
Type: Timestamp  
Required: No

 ** failureMessage **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-failureMessage"></a>
An error message.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-lastModifiedTime"></a>
When the invocation was last modified.  
Type: Timestamp  
Required: No

 ** status **   <a name="bedrock-Type-runtime_AsyncInvokeSummary-status"></a>
The invocation's status.  
Type: String  
Valid Values: `InProgress | Completed | Failed`   
Required: No

## See Also
<a name="API_runtime_AsyncInvokeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/AsyncInvokeSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/AsyncInvokeSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/AsyncInvokeSummary) 