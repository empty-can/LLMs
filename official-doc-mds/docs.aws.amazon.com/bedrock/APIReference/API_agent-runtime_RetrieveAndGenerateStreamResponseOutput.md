

# RetrieveAndGenerateStreamResponseOutput
<a name="API_agent-runtime_RetrieveAndGenerateStreamResponseOutput"></a>

A retrieve and generate stream response output.

## Contents
<a name="API_agent-runtime_RetrieveAndGenerateStreamResponseOutput_Contents"></a>

 ** accessDeniedException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-accessDeniedException"></a>
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** badGatewayException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-badGatewayException"></a>
The request failed due to a bad gateway error.  
Type: Exception  
HTTP Status Code: 502  
Required: No

 ** citation **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-citation"></a>
A citation event.  
Type: [CitationEvent](API_agent-runtime_CitationEvent.md) object  
Required: No

 ** conflictException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-conflictException"></a>
Error occurred because of a conflict while performing an operation.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** dependencyFailedException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-dependencyFailedException"></a>
The request failed due to a dependency error.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** guardrail **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-guardrail"></a>
A guardrail event.  
Type: [GuardrailEvent](API_agent-runtime_GuardrailEvent.md) object  
Required: No

 ** internalServerException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** output **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-output"></a>
An output event.  
Type: [RetrieveAndGenerateOutputEvent](API_agent-runtime_RetrieveAndGenerateOutputEvent.md) object  
Required: No

 ** resourceNotFoundException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-resourceNotFoundException"></a>
The specified resource ARN was not found. For troubleshooting this error, see [ResourceNotFound](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** serviceQuotaExceededException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-serviceQuotaExceededException"></a>
Your request exceeds the service quota for your account. You can view your quotas at [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html). You can resubmit your request later.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** throttlingException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-throttlingException"></a>
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="bedrock-Type-agent-runtime_RetrieveAndGenerateStreamResponseOutput-validationException"></a>
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_agent-runtime_RetrieveAndGenerateStreamResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStreamResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStreamResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStreamResponseOutput) 