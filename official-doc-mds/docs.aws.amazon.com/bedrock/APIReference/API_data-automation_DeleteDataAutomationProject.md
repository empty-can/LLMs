

# DeleteDataAutomationProject
<a name="API_data-automation_DeleteDataAutomationProject"></a>

Deletes a data automation project.

## Request Syntax
<a name="API_data-automation_DeleteDataAutomationProject_RequestSyntax"></a>

```
DELETE /data-automation-projects/{{projectArn}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_data-automation_DeleteDataAutomationProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectArn](#API_data-automation_DeleteDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_DeleteDataAutomationProject-request-uri-projectArn"></a>
The project's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_DeleteDataAutomationProject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_data-automation_DeleteDataAutomationProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "projectArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation_DeleteDataAutomationProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [projectArn](#API_data-automation_DeleteDataAutomationProject_ResponseSyntax) **   <a name="bedrock-data-automation_DeleteDataAutomationProject-response-projectArn"></a>
The project's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}` 

 ** [status](#API_data-automation_DeleteDataAutomationProject_ResponseSyntax) **   <a name="bedrock-data-automation_DeleteDataAutomationProject-response-status"></a>
The project's status.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED` 

## Errors
<a name="API_data-automation_DeleteDataAutomationProject_Errors"></a>

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
<a name="API_data-automation_DeleteDataAutomationProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DeleteDataAutomationProject) 