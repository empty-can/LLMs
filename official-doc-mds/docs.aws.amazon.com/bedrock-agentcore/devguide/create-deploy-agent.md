

# Create and deploy your agent
<a name="create-deploy-agent"></a>

If you have an agent already up and running in AgentCore Runtime, you can skip the following steps

**Topics**
+ [Pick a supported framework](#supported-frameworks)
+ [Create and deploy your agent](#create-deploy-agent-steps)

## Pick a supported framework
<a name="supported-frameworks"></a>

AgentCore Evaluations currently supports the following agentic frameworks and instrumentation libraries
+ Strands Agent
+ LangGraph configured with one of the following instrumentation libraries
  +  `opentelemetry-instrumentation-langchain` 
  +  `openinference-instrumentation-langchain` 

## Create and deploy your agent
<a name="create-deploy-agent-steps"></a>

Create and deploy your agent by following the [Get Started guide for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started.html) . Setup observability using [Get started with AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html) . You can find additional examples in the [AgentCore Evaluations Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations).