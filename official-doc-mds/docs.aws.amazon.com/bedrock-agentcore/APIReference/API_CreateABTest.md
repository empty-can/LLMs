

# CreateABTest
<a name="API_CreateABTest"></a>

Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.

## Request Syntax
<a name="API_CreateABTest_RequestSyntax"></a>

```
POST /ab-tests HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "enableOnCreate": {{boolean}},
   "evaluationConfig": { ... },
   "gatewayArn": "{{string}}",
   "gatewayFilter": { 
      "targetPaths": [ "{{string}}" ]
   },
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "variants": [ 
      { 
         "name": "{{string}}",
         "variantConfiguration": { 
            "configurationBundle": { 
               "bundleArn": "{{string}}",
               "bundleVersion": "{{string}}"
            },
            "target": { 
               "name": "{{string}}"
            }
         },
         "weight": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateABTest_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateABTest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-description"></a>
The description of the A/B test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [enableOnCreate](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-enableOnCreate"></a>
Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.  
Type: Boolean  
Required: No

 ** [evaluationConfig](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-evaluationConfig"></a>
The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.  
Type: [ABTestEvaluationConfig](API_ABTestEvaluationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [gatewayArn](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-gatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** [gatewayFilter](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-gatewayFilter"></a>
Optional filter to restrict which gateway target paths are included in the A/B test.  
Type: [GatewayFilter](API_GatewayFilter.md) object  
Required: No

 ** [name](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-name"></a>
The name of the A/B test. Must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [roleArn](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-roleArn"></a>
The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [tags](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-tags"></a>
A map of tag keys and values to associate with the A/B test.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [variants](#API_CreateABTest_RequestSyntax) **   <a name="BedrockAgentCore-CreateABTest-request-variants"></a>
The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.  
Type: Array of [Variant](API_Variant.md) objects  
Array Members: Fixed number of 2 items.  
Required: Yes

## Response Syntax
<a name="API_CreateABTest_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "abTestArn": "string",
   "abTestId": "string",
   "createdAt": number,
   "executionStatus": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateABTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [abTestArn](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-abTestArn"></a>
The Amazon Resource Name (ARN) of the created A/B test.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [abTestId](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-abTestId"></a>
The unique identifier of the created A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-createdAt"></a>
The timestamp when the A/B test was created.  
Type: Timestamp

 ** [executionStatus](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-executionStatus"></a>
The execution status indicating whether the A/B test is currently running.  
Type: String  
Valid Values: `PAUSED | RUNNING | STOPPED | NOT_STARTED` 

 ** [name](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-name"></a>
The name of the A/B test.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [status](#API_CreateABTest_ResponseSyntax) **   <a name="BedrockAgentCore-CreateABTest-response-status"></a>
The status of the A/B test.  
Type: String  
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED | FAILED` 

## Errors
<a name="API_CreateABTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateABTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/CreateABTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CreateABTest) 