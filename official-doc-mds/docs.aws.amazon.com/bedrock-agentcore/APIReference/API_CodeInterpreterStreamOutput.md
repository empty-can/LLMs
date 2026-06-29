

# CodeInterpreterStreamOutput
<a name="API_CodeInterpreterStreamOutput"></a>

Contains output from a code interpreter stream.

## Contents
<a name="API_CodeInterpreterStreamOutput_Contents"></a>

 ** accessDeniedException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-accessDeniedException"></a>
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** conflictException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-conflictException"></a>
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** internalServerException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** resourceNotFoundException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** result **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-result"></a>
The output produced by executing code in a code interpreter session in Amazon Bedrock AgentCore. This structure contains the results of code execution, including textual output, structured data, and error information. Agents use these results to generate responses that incorporate computation, data analysis, and visualization.  
Type: [CodeInterpreterResult](API_CodeInterpreterResult.md) object  
Required: No

 ** serviceQuotaExceededException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402  
Required: No

 ** throttlingException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="BedrockAgentCore-Type-CodeInterpreterStreamOutput-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_CodeInterpreterStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CodeInterpreterStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CodeInterpreterStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CodeInterpreterStreamOutput) 