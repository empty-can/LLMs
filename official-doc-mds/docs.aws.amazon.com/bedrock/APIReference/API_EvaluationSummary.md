

# EvaluationSummary
<a name="API_EvaluationSummary"></a>

Summary information of an evaluation job.

## Contents
<a name="API_EvaluationSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-EvaluationSummary-creationTime"></a>
The time the evaluation job was created.  
Type: Timestamp  
Required: Yes

 ** evaluationTaskTypes **   <a name="bedrock-Type-EvaluationSummary-evaluationTaskTypes"></a>
The type of task for model evaluation.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-Za-z0-9]+`   
Valid Values: `Summarization | Classification | QuestionAndAnswer | Generation | Custom`   
Required: Yes

 ** jobArn **   <a name="bedrock-Type-EvaluationSummary-jobArn"></a>
The Amazon Resource Name (ARN) of the evaluation job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12}`   
Required: Yes

 ** jobName **   <a name="bedrock-Type-EvaluationSummary-jobName"></a>
The name for the evaluation job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}`   
Required: Yes

 ** jobType **   <a name="bedrock-Type-EvaluationSummary-jobType"></a>
Specifies whether the evaluation job is automated or human-based.  
Type: String  
Valid Values: `Human | Automated`   
Required: Yes

 ** status **   <a name="bedrock-Type-EvaluationSummary-status"></a>
The current status of the evaluation job.  
Type: String  
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting`   
Required: Yes

 ** applicationType **   <a name="bedrock-Type-EvaluationSummary-applicationType"></a>
Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).  
Type: String  
Valid Values: `ModelEvaluation | RagEvaluation`   
Required: No

 ** customMetricsEvaluatorModelIdentifiers **   <a name="bedrock-Type-EvaluationSummary-customMetricsEvaluatorModelIdentifiers"></a>
The Amazon Resource Names (ARNs) of the models used to compute custom metrics in an Amazon Bedrock evaluation job.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:inference-profile/(([a-z-]{2,8}.)[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))))$|(^[a-z0-9-]+[.][a-z0-9-]+([.][a-z0-9-]+)*(:[a-z0-9-]+)?$)|^[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: No

 ** evaluatorModelIdentifiers **   <a name="bedrock-Type-EvaluationSummary-evaluatorModelIdentifiers"></a>
The Amazon Resource Names (ARNs) of the models used to compute the metrics for a knowledge base evaluation job.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:inference-profile/(([a-z-]{2,8}.)[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))))$|(^[a-z0-9-]+[.][a-z0-9-]+([.][a-z0-9-]+)*(:[a-z0-9-]+)?$)|^[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: No

 ** inferenceConfigSummary **   <a name="bedrock-Type-EvaluationSummary-inferenceConfigSummary"></a>
Identifies the models, Knowledge Bases, or other RAG sources evaluated in a model or Knowledge Base evaluation job.  
Type: [EvaluationInferenceConfigSummary](API_EvaluationInferenceConfigSummary.md) object  
Required: No

 ** modelIdentifiers **   <a name="bedrock-Type-EvaluationSummary-modelIdentifiers"></a>
 *This member has been deprecated.*   
The Amazon Resource Names (ARNs) of the model(s) used for the evaluation job.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:((:foundation-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|([0-9]{12}:provisioned-model/[a-z0-9]{12})|([0-9]{12}:imported-model/[a-z0-9]{12})|([0-9]{12}:application-inference-profile/[a-z0-9]{12})|([0-9]{12}:inference-profile/(([a-z-]{2,8}.)[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))|([0-9]{12}:(default-prompt-router|prompt-router)/[a-zA-Z0-9-:.]+)))|(([a-z]{2,4}[.]{1})([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63})))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.:]?[a-z0-9-]{1,63}))|arn:aws(-[^:]+)?:sagemaker:[a-z0-9-]{1,20}:[0-9]{12}:endpoint/[a-z0-9-]{1,63}`   
Required: No

 ** ragIdentifiers **   <a name="bedrock-Type-EvaluationSummary-ragIdentifiers"></a>
 *This member has been deprecated.*   
The Amazon Resource Names (ARNs) of the knowledge base resources used for a knowledge base evaluation job.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: No

## See Also
<a name="API_EvaluationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationSummary) 