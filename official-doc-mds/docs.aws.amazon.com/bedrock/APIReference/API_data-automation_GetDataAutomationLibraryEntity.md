

# GetDataAutomationLibraryEntity
<a name="API_data-automation_GetDataAutomationLibraryEntity"></a>

Gets details about a data automation library entity.

## Request Syntax
<a name="API_data-automation_GetDataAutomationLibraryEntity_RequestSyntax"></a>

```
POST /data-automation-libraries/{{libraryArn}}/entityType/{{entityType}}/entities/{{entityId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_data-automation_GetDataAutomationLibraryEntity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [entityId](#API_data-automation_GetDataAutomationLibraryEntity_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryEntity-request-uri-entityId"></a>
The entity ID.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** [entityType](#API_data-automation_GetDataAutomationLibraryEntity_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryEntity-request-uri-entityType"></a>
The entity type.  
Valid Values: `VOCABULARY`   
Required: Yes

 ** [libraryArn](#API_data-automation_GetDataAutomationLibraryEntity_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryEntity-request-uri-libraryArn"></a>
The library's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_GetDataAutomationLibraryEntity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_data-automation_GetDataAutomationLibraryEntity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entity": { ... }
}
```

## Response Elements
<a name="API_data-automation_GetDataAutomationLibraryEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entity](#API_data-automation_GetDataAutomationLibraryEntity_ResponseSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibraryEntity-response-entity"></a>
Details about the entity.  
Type: [EntityDetails](API_data-automation_EntityDetails.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_data-automation_GetDataAutomationLibraryEntity_Errors"></a>

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
<a name="API_data-automation_GetDataAutomationLibraryEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibraryEntity) 