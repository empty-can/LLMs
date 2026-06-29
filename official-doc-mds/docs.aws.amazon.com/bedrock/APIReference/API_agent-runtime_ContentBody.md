

# ContentBody
<a name="API_agent-runtime_ContentBody"></a>

Contains the body of the API response.

This data type is used in the following API operations:
+ In the `returnControlInvocationResults` field of the [InvokeAgent request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_RequestSyntax) 

## Contents
<a name="API_agent-runtime_ContentBody_Contents"></a>

 ** body **   <a name="bedrock-Type-agent-runtime_ContentBody-body"></a>
The body of the API response.  
Type: String  
Required: No

 ** images **   <a name="bedrock-Type-agent-runtime_ContentBody-images"></a>
Lists details, including format and source, for the image in the response from the function call. You can specify only one image and the function in the `returnControlInvocationResults` must be a computer use action. For more information, see [Configure an Amazon Bedrock Agent to complete tasks with computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html).   
Type: Array of [ImageInput](API_agent-runtime_ImageInput.md) objects  
Required: No

## See Also
<a name="API_agent-runtime_ContentBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ContentBody) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ContentBody) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ContentBody) 