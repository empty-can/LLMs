

# GetBlueprintOptimizationStatus
<a name="API_data-automation_GetBlueprintOptimizationStatus"></a>

Gets the status of a blueprint optimization job.

## Request Syntax
<a name="API_data-automation_GetBlueprintOptimizationStatus_RequestSyntax"></a>

```
POST /getBlueprintOptimizationStatus/{{invocationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_data-automation_GetBlueprintOptimizationStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [invocationArn](#API_data-automation_GetBlueprintOptimizationStatus_RequestSyntax) **   <a name="bedrock-data-automation_GetBlueprintOptimizationStatus-request-uri-invocationArn"></a>
The ARN of the optimization job invocation.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:blueprint-optimization-invocation/[a-zA-Z0-9-_]+`   
Required: Yes

## Request Body
<a name="API_data-automation_GetBlueprintOptimizationStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_data-automation_GetBlueprintOptimizationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorMessage": "string",
   "errorType": "string",
   "outputConfiguration": { 
      "s3Object": { 
         "s3Uri": "string",
         "version": "string"
      }
   },
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation_GetBlueprintOptimizationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorMessage](#API_data-automation_GetBlueprintOptimizationStatus_ResponseSyntax) **   <a name="bedrock-data-automation_GetBlueprintOptimizationStatus-response-errorMessage"></a>
The error message if the job failed.  
Type: String

 ** [errorType](#API_data-automation_GetBlueprintOptimizationStatus_ResponseSyntax) **   <a name="bedrock-data-automation_GetBlueprintOptimizationStatus-response-errorType"></a>
The type of error if the job failed.  
Type: String

 ** [outputConfiguration](#API_data-automation_GetBlueprintOptimizationStatus_ResponseSyntax) **   <a name="bedrock-data-automation_GetBlueprintOptimizationStatus-response-outputConfiguration"></a>
The location of the optimization results.  
Type: [BlueprintOptimizationOutputConfiguration](API_data-automation_BlueprintOptimizationOutputConfiguration.md) object

 ** [status](#API_data-automation_GetBlueprintOptimizationStatus_ResponseSyntax) **   <a name="bedrock-data-automation_GetBlueprintOptimizationStatus-response-status"></a>
The job's status.  
Type: String  
Valid Values: `Created | InProgress | Success | ServiceError | ClientError` 

## Errors
<a name="API_data-automation_GetBlueprintOptimizationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_GetBlueprintOptimizationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/GetBlueprintOptimizationStatus) 