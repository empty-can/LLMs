

# DeleteDataAutomationLibrary
<a name="API_data-automation_DeleteDataAutomationLibrary"></a>

Deletes a data automation library.

## Request Syntax
<a name="API_data-automation_DeleteDataAutomationLibrary_RequestSyntax"></a>

```
DELETE /data-automation-libraries/{{libraryArn}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_data-automation_DeleteDataAutomationLibrary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [libraryArn](#API_data-automation_DeleteDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_DeleteDataAutomationLibrary-request-uri-libraryArn"></a>
The library's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_DeleteDataAutomationLibrary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_data-automation_DeleteDataAutomationLibrary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "libraryArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation_DeleteDataAutomationLibrary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [libraryArn](#API_data-automation_DeleteDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_DeleteDataAutomationLibrary-response-libraryArn"></a>
The library's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}` 

 ** [status](#API_data-automation_DeleteDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_DeleteDataAutomationLibrary-response-status"></a>
The library's status.  
Type: String  
Valid Values: `ACTIVE | DELETING` 

## Errors
<a name="API_data-automation_DeleteDataAutomationLibrary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** ConflictException **   
  
HTTP Status Code: 409

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_DeleteDataAutomationLibrary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DeleteDataAutomationLibrary) 