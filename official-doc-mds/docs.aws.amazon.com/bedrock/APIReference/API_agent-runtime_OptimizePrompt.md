

# OptimizePrompt
<a name="API_agent-runtime_OptimizePrompt"></a>

Optimizes a prompt for the task that you specify. For more information, see [Optimize a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html).

## Request Syntax
<a name="API_agent-runtime_OptimizePrompt_RequestSyntax"></a>

```
POST /optimize-prompt HTTP/1.1
Content-type: application/json

{
   "input": { ... },
   "targetModelId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent-runtime_OptimizePrompt_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent-runtime_OptimizePrompt_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [input](#API_agent-runtime_OptimizePrompt_RequestSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-request-input"></a>
Contains the prompt to optimize.  
Type: [InputPrompt](API_agent-runtime_InputPrompt.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [targetModelId](#API_agent-runtime_OptimizePrompt_RequestSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-request-targetModelId"></a>
The unique identifier of the model that you want to optimize the prompt for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:provisioned-model/[a-z0-9]{12})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

## Response Syntax
<a name="API_agent-runtime_OptimizePrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "analyzePromptEvent": { 
      "message": "string"
   },
   "badGatewayException": { 
   },
   "dependencyFailedException": { 
   },
   "internalServerException": { 
   },
   "optimizedPromptEvent": { 
      "optimizedPrompt": { ... }
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_agent-runtime_OptimizePrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403

 ** [analyzePromptEvent](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-analyzePromptEvent"></a>
An event in which the prompt was analyzed in preparation for optimization.  
Type: [AnalyzePromptEvent](API_agent-runtime_AnalyzePromptEvent.md) object

 ** [badGatewayException](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.  
Type: Exception  
HTTP Status Code: 502

 ** [dependencyFailedException](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424

 ** [internalServerException](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500

 ** [optimizedPromptEvent](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-optimizedPromptEvent"></a>
An event in which the prompt was optimized.  
Type: [OptimizedPromptEvent](API_agent-runtime_OptimizedPromptEvent.md) object

 ** [throttlingException](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-throttlingException"></a>
Your request was throttled because of service-wide limitations. Resubmit your request later or in a different region. You can also purchase [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) to increase the rate or number of tokens you can process.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_agent-runtime_OptimizePrompt_ResponseSyntax) **   <a name="bedrock-agent-runtime_OptimizePrompt-response-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_agent-runtime_OptimizePrompt_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_OptimizePrompt_Examples"></a>

### Example
<a name="API_agent-runtime_OptimizePrompt_Example_1"></a>

This example illustrates one usage of OptimizePrompt.

```
POST /optimize-prompt HTTP/1.1
Content-type: application/json

{
    "input": {
        "textPrompt": {
            "text": "Please summarize this text: "
        }
    },
    "targetModelId": "anthropic.claude-3-sonnet-20240229-v1:0"
}
```

## See Also
<a name="API_agent-runtime_OptimizePrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/OptimizePrompt) 