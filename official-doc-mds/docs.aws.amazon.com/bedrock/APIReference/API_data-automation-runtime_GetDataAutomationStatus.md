

# GetDataAutomationStatus
<a name="API_data-automation-runtime_GetDataAutomationStatus"></a>

Gets details about a data automation invocation. To process data, start an invocation with [InvokeDataAutomationAsync](API_data-automation-runtime_InvokeDataAutomationAsync.md). When the status is `Success`, retrieve the output from the S3 bucket.

## Request Syntax
<a name="API_data-automation-runtime_GetDataAutomationStatus_RequestSyntax"></a>

```
{
   "invocationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_data-automation-runtime_GetDataAutomationStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [invocationArn](#API_data-automation-runtime_GetDataAutomationStatus_RequestSyntax) **   <a name="bedrock-data-automation-runtime_GetDataAutomationStatus-request-invocationArn"></a>
The invocation ARN returned by [InvokeDataAutomationAsync](API_data-automation-runtime_InvokeDataAutomationAsync.md).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:(insights-invocation|data-automation-invocation)/[a-zA-Z0-9-_]+`   
Required: Yes

## Response Syntax
<a name="API_data-automation-runtime_GetDataAutomationStatus_ResponseSyntax"></a>

```
{
   "errorMessage": "string",
   "errorType": "string",
   "outputConfiguration": { 
      "s3Uri": "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation-runtime_GetDataAutomationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorMessage](#API_data-automation-runtime_GetDataAutomationStatus_ResponseSyntax) **   <a name="bedrock-data-automation-runtime_GetDataAutomationStatus-response-errorMessage"></a>
If an error ocurred, the error message.  
Type: String

 ** [errorType](#API_data-automation-runtime_GetDataAutomationStatus_ResponseSyntax) **   <a name="bedrock-data-automation-runtime_GetDataAutomationStatus-response-errorType"></a>
If an error ocurred, the error's type.  
Type: String

 ** [outputConfiguration](#API_data-automation-runtime_GetDataAutomationStatus_ResponseSyntax) **   <a name="bedrock-data-automation-runtime_GetDataAutomationStatus-response-outputConfiguration"></a>
The path of the output metadata object.  
Type: [OutputConfiguration](API_data-automation-runtime_OutputConfiguration.md) object

 ** [status](#API_data-automation-runtime_GetDataAutomationStatus_ResponseSyntax) **   <a name="bedrock-data-automation-runtime_GetDataAutomationStatus-response-status"></a>
The invocation's status.  
Type: String  
Valid Values: `Created | InProgress | Success | ServiceError | ClientError` 

## Errors
<a name="API_data-automation-runtime_GetDataAutomationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 400

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 400

 ** ThrottlingException **   
  
HTTP Status Code: 400

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation-runtime_GetDataAutomationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/GetDataAutomationStatus) 