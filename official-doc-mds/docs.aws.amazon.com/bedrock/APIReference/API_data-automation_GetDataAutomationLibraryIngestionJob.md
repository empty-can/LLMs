

# GetDataAutomationLibraryIngestionJob
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob"></a>

Gets details about a data automation library ingestion job.

## Request Syntax
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_RequestSyntax"></a>

```
POST /data-automation-libraries/{{libraryArn}}/library-ingestion-jobs/{{jobArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobArn](#API_data-automation_GetDataAutomationLibraryIngestionJob_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryIngestionJob-request-uri-jobArn"></a>
The job's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library-ingestion-job/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** [libraryArn](#API_data-automation_GetDataAutomationLibraryIngestionJob_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryIngestionJob-request-uri-libraryArn"></a>
The library's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "job": { 
      "completionTime": "string",
      "creationTime": "string",
      "entityType": "string",
      "errorMessage": "string",
      "errorType": "string",
      "jobArn": "string",
      "jobStatus": "string",
      "operationType": "string",
      "outputConfiguration": { 
         "s3Uri": "string"
      }
   }
}
```

## Response Elements
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [job](#API_data-automation_GetDataAutomationLibraryIngestionJob_ResponseSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryIngestionJob-response-job"></a>
Details about the job.  
Type: [DataAutomationLibraryIngestionJob](API_data-automation_DataAutomationLibraryIngestionJob.md) object

## Errors
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_Errors"></a>

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
<a name="API_data-automation_GetDataAutomationLibraryIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryIngestionJob) 