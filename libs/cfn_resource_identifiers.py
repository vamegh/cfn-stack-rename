def resources():
    # from Former2 - https://github.com/iann0036/former2/blob/master/util/importable.txt
    return {
        "AWS::ACMPCA::Certificate": {
            "importProperties": [
                "Arn",
                "CertificateAuthorityArn"
            ]
        },
        "AWS::ACMPCA::CertificateAuthority": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ACMPCA::CertificateAuthorityActivation": {
            "importProperties": [
                "CertificateAuthorityArn"
            ]
        },
        "AWS::ACMPCA::Permission": {
            "importProperties": [
                "CertificateAuthorityArn",
                "Principal"
            ]
        },
        "AWS::APS::RuleGroupsNamespace": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::APS::Workspace": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::AccessAnalyzer::Analyzer": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Amplify::App": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Amplify::Branch": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Amplify::Domain": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::AmplifyUIBuilder::Component": {
            "importProperties": [
                "AppId",
                "EnvironmentName",
                "Id"
            ]
        },
        "AWS::AmplifyUIBuilder::Theme": {
            "importProperties": [
                "AppId",
                "EnvironmentName",
                "Id"
            ]
        },
        "AWS::ApiGateway::Account": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ApiGateway::ApiKey": {
            "importProperties": [
                "APIKeyId"
            ]
        },
        "AWS::ApiGateway::Authorizer": {
            "importProperties": [
                "RestApiId",
                "AuthorizerId"
            ]
        },
        "AWS::ApiGateway::BasePathMapping": {
            "importProperties": [
                "DomainName",
                "BasePath"
            ]
        },
        "AWS::ApiGateway::ClientCertificate": {
            "importProperties": [
                "ClientCertificateId"
            ]
        },
        "AWS::ApiGateway::Deployment": {
            "importProperties": [
                "RestApiId"
            ]
        },
        "AWS::ApiGateway::DocumentationVersion": {
            "importProperties": [
                "DocumentationVersion",
                "RestApiId"
            ]
        },
        "AWS::ApiGateway::DomainName": {
            "importProperties": [
                "DomainName"
            ]
        },
        "AWS::ApiGateway::Method": {
            "importProperties": [
                "RestApiId",
                "ResourceId",
                "HttpMethod"
            ]
        },
        "AWS::ApiGateway::Model": {
            "importProperties": [
                "RestApiId",
                "Name"
            ]
        },
        "AWS::ApiGateway::RequestValidator": {
            "importProperties": [
                "RestApiId",
                "RequestValidatorId"
            ]
        },
        "AWS::ApiGateway::Resource": {
            "importProperties": [
                "RestApiId",
                "ResourceId"
            ]
        },
        "AWS::ApiGateway::RestApi": {
            "importProperties": [
                "RestApiId"
            ]
        },
        "AWS::ApiGateway::Stage": {
            "importProperties": [
                "RestApiId",
                "StageName"
            ]
        },
        "AWS::ApiGateway::UsagePlan": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ApiGateway::UsagePlanKey": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::AppFlow::ConnectorProfile": {
            "importProperties": [
                "ConnectorProfileName"
            ]
        },
        "AWS::AppFlow::Flow": {
            "importProperties": [
                "FlowName"
            ]
        },
        "AWS::AppIntegrations::DataIntegration": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::AppIntegrations::EventIntegration": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::AppRunner::Service": {
            "importProperties": [
                "ServiceArn"
            ]
        },
        "AWS::AppRunner::VpcConnector": {
            "importProperties": [
                "VpcConnectorArn"
            ]
        },
        "AWS::AppStream::AppBlock": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::AppStream::Application": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::AppStream::ApplicationEntitlementAssociation": {
            "importProperties": [
                "StackName",
                "EntitlementName",
                "ApplicationIdentifier"
            ]
        },
        "AWS::AppStream::ApplicationFleetAssociation": {
            "importProperties": [
                "FleetName",
                "ApplicationArn"
            ]
        },
        "AWS::AppStream::Entitlement": {
            "importProperties": [
                "StackName",
                "Name"
            ]
        },
        "AWS::AppSync::DomainName": {
            "importProperties": [
                "DomainName"
            ]
        },
        "AWS::AppSync::DomainNameApiAssociation": {
            "importProperties": [
                "ApiAssociationIdentifier"
            ]
        },
        "AWS::ApplicationInsights::Application": {
            "importProperties": [
                "ApplicationARN"
            ]
        },
        "AWS::Athena::DataCatalog": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Athena::NamedQuery": {
            "importProperties": [
                "NamedQueryId"
            ]
        },
        "AWS::Athena::PreparedStatement": {
            "importProperties": [
                "StatementName",
                "WorkGroup"
            ]
        },
        "AWS::Athena::WorkGroup": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::AuditManager::Assessment": {
            "importProperties": [
                "AssessmentId"
            ]
        },
        "AWS::AutoScaling::AutoScalingGroup": {
            "importProperties": [
                "AutoScalingGroupName"
            ]
        },
        "AWS::AutoScaling::LaunchConfiguration": {
            "importProperties": [
                "LaunchConfigurationName"
            ]
        },
        "AWS::AutoScaling::LifecycleHook": {
            "importProperties": [
                "AutoScalingGroupName",
                "LifecycleHookName"
            ]
        },
        "AWS::AutoScaling::ScalingPolicy": {
            "importProperties": [
                "PolicyName"
            ]
        },
        "AWS::AutoScaling::ScheduledAction": {
            "importProperties": [
                "ScheduledActionName"
            ]
        },
        "AWS::AutoScaling::WarmPool": {
            "importProperties": [
                "AutoScalingGroupName"
            ]
        },
        "AWS::Backup::BackupPlan": {
            "importProperties": [
                "BackupPlanId"
            ]
        },
        "AWS::Backup::BackupSelection": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Backup::BackupVault": {
            "importProperties": [
                "BackupVaultName"
            ]
        },
        "AWS::Backup::Framework": {
            "importProperties": [
                "FrameworkArn"
            ]
        },
        "AWS::Backup::ReportPlan": {
            "importProperties": [
                "ReportPlanArn"
            ]
        },
        "AWS::Batch::ComputeEnvironment": {
            "importProperties": [
                "ComputeEnvironmentArn"
            ]
        },
        "AWS::Batch::JobQueue": {
            "importProperties": [
                "JobQueueArn"
            ]
        },
        "AWS::Batch::SchedulingPolicy": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Budgets::BudgetsAction": {
            "importProperties": [
                "ActionId",
                "BudgetName"
            ]
        },
        "AWS::CE::AnomalyMonitor": {
            "importProperties": [
                "MonitorArn"
            ]
        },
        "AWS::CE::AnomalySubscription": {
            "importProperties": [
                "SubscriptionArn"
            ]
        },
        "AWS::CE::CostCategory": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CUR::ReportDefinition": {
            "importProperties": [
                "ReportName"
            ]
        },
        "AWS::Cassandra::Keyspace": {
            "importProperties": [
                "KeyspaceName"
            ]
        },
        "AWS::Cassandra::Table": {
            "importProperties": [
                "KeyspaceName",
                "TableName"
            ]
        },
        "AWS::CertificateManager::Account": {
            "importProperties": [
                "AccountId"
            ]
        },
        "AWS::Chatbot::SlackChannelConfiguration": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::HookDefaultVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::HookTypeConfig": {
            "importProperties": [
                "TypeArn"
            ]
        },
        "AWS::CloudFormation::HookVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::ModuleDefaultVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::ModuleVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::PublicTypeVersion": {
            "importProperties": [
                "PublicTypeArn"
            ]
        },
        "AWS::CloudFormation::Publisher": {
            "importProperties": [
                "PublisherId"
            ]
        },
        "AWS::CloudFormation::ResourceDefaultVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::ResourceVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFormation::Stack": {
            "importProperties": [
                "StackId"
            ]
        },
        "AWS::CloudFormation::StackSet": {
            "importProperties": [
                "StackSetId"
            ]
        },
        "AWS::CloudFormation::TypeActivation": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFront::CachePolicy": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudFront::CloudFrontOriginAccessIdentity": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudFront::Distribution": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudFront::Function": {
            "importProperties": [
                "FunctionARN"
            ]
        },
        "AWS::CloudFront::KeyGroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudFront::OriginRequestPolicy": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudFront::PublicKey": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudFront::RealtimeLogConfig": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CloudFront::ResponseHeadersPolicy": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::CloudTrail::Trail": {
            "importProperties": [
                "TrailName"
            ]
        },
        "AWS::CloudWatch::Alarm": {
            "importProperties": [
                "AlarmName"
            ]
        },
        "AWS::CloudWatch::CompositeAlarm": {
            "importProperties": [
                "AlarmName"
            ]
        },
        "AWS::CloudWatch::MetricStream": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::CodeArtifact::Domain": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CodeArtifact::Repository": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::CodeGuruProfiler::ProfilingGroup": {
            "importProperties": [
                "ProfilingGroupName"
            ]
        },
        "AWS::CodeGuruReviewer::RepositoryAssociation": {
            "importProperties": [
                "AssociationArn"
            ]
        },
        "AWS::CodeStarConnections::Connection": {
            "importProperties": [
                "ConnectionArn"
            ]
        },
        "AWS::CodeStarNotifications::NotificationRule": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Config::AggregationAuthorization": {
            "importProperties": [
                "AggregationAuthorizationArn"
            ]
        },
        "AWS::Config::ConfigurationAggregator": {
            "importProperties": [
                "ConfigurationAggregatorName"
            ]
        },
        "AWS::Config::ConformancePack": {
            "importProperties": [
                "ConformancePackName"
            ]
        },
        "AWS::Config::OrganizationConformancePack": {
            "importProperties": [
                "OrganizationConformancePackName"
            ]
        },
        "AWS::Config::StoredQuery": {
            "importProperties": [
                "QueryName"
            ]
        },
        "AWS::Connect::ContactFlow": {
            "importProperties": [
                "ContactFlowArn"
            ]
        },
        "AWS::Connect::ContactFlowModule": {
            "importProperties": [
                "ContactFlowModuleArn"
            ]
        },
        "AWS::Connect::HoursOfOperation": {
            "importProperties": [
                "HoursOfOperationArn"
            ]
        },
        "AWS::Connect::QuickConnect": {
            "importProperties": [
                "QuickConnectArn"
            ]
        },
        "AWS::Connect::User": {
            "importProperties": [
                "UserArn"
            ]
        },
        "AWS::Connect::UserHierarchyGroup": {
            "importProperties": [
                "UserHierarchyGroupArn"
            ]
        },
        "AWS::CustomerProfiles::Domain": {
            "importProperties": [
                "DomainName"
            ]
        },
        "AWS::CustomerProfiles::Integration": {
            "importProperties": [
                "DomainName",
                "Uri"
            ]
        },
        "AWS::CustomerProfiles::ObjectType": {
            "importProperties": [
                "DomainName",
                "ObjectTypeName"
            ]
        },
        "AWS::DataBrew::Dataset": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::DataBrew::Job": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::DataBrew::Project": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::DataBrew::Recipe": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::DataBrew::Ruleset": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::DataBrew::Schedule": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::DataSync::Agent": {
            "importProperties": [
                "AgentArn"
            ]
        },
        "AWS::DataSync::LocationEFS": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::LocationFSxWindows": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::LocationHDFS": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::LocationNFS": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::LocationObjectStorage": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::LocationS3": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::LocationSMB": {
            "importProperties": [
                "LocationArn"
            ]
        },
        "AWS::DataSync::Task": {
            "importProperties": [
                "TaskArn"
            ]
        },
        "AWS::Detective::Graph": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Detective::MemberInvitation": {
            "importProperties": [
                "GraphArn",
                "MemberId"
            ]
        },
        "AWS::DevOpsGuru::NotificationChannel": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::DevOpsGuru::ResourceCollection": {
            "importProperties": [
                "ResourceCollectionType"
            ]
        },
        "AWS::DynamoDB::GlobalTable": {
            "importProperties": [
                "TableName"
            ]
        },
        "AWS::DynamoDB::Table": {
            "importProperties": [
                "TableName"
            ]
        },
        "AWS::EC2::CapacityReservationFleet": {
            "importProperties": [
                "CapacityReservationFleetId"
            ]
        },
        "AWS::EC2::CarrierGateway": {
            "importProperties": [
                "CarrierGatewayId"
            ]
        },
        "AWS::EC2::DHCPOptions": {
            "importProperties": [
                "DhcpOptionsId"
            ]
        },
        "AWS::EC2::EC2Fleet": {
            "importProperties": [
                "FleetId"
            ]
        },
        "AWS::EC2::EIP": {
            "importProperties": [
                "PublicIp"
            ]
        },
        "AWS::EC2::EgressOnlyInternetGateway": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::EnclaveCertificateIamRoleAssociation": {
            "importProperties": [
                "CertificateArn",
                "RoleArn"
            ]
        },
        "AWS::EC2::FlowLog": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::GatewayRouteTableAssociation": {
            "importProperties": [
                "GatewayId"
            ]
        },
        "AWS::EC2::Host": {
            "importProperties": [
                "HostId"
            ]
        },
        "AWS::EC2::IPAM": {
            "importProperties": [
                "IpamId"
            ]
        },
        "AWS::EC2::IPAMAllocation": {
            "importProperties": [
                "IpamPoolId",
                "IpamPoolAllocationId",
                "Cidr"
            ]
        },
        "AWS::EC2::IPAMPool": {
            "importProperties": [
                "IpamPoolId"
            ]
        },
        "AWS::EC2::IPAMScope": {
            "importProperties": [
                "IpamScopeId"
            ]
        },
        "AWS::EC2::Instance": {
            "importProperties": [
                "InstanceId"
            ]
        },
        "AWS::EC2::InternetGateway": {
            "importProperties": [
                "InternetGatewayId"
            ]
        },
        "AWS::EC2::LocalGatewayRoute": {
            "importProperties": [
                "DestinationCidrBlock",
                "LocalGatewayRouteTableId"
            ]
        },
        "AWS::EC2::LocalGatewayRouteTableVPCAssociation": {
            "importProperties": [
                "LocalGatewayRouteTableVpcAssociationId"
            ]
        },
        "AWS::EC2::NatGateway": {
            "importProperties": [
                "NatGatewayId"
            ]
        },
        "AWS::EC2::NetworkAcl": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::NetworkInsightsAccessScope": {
            "importProperties": [
                "NetworkInsightsAccessScopeId"
            ]
        },
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis": {
            "importProperties": [
                "NetworkInsightsAccessScopeAnalysisId"
            ]
        },
        "AWS::EC2::NetworkInsightsAnalysis": {
            "importProperties": [
                "NetworkInsightsAnalysisId"
            ]
        },
        "AWS::EC2::NetworkInsightsPath": {
            "importProperties": [
                "NetworkInsightsPathId"
            ]
        },
        "AWS::EC2::NetworkInterface": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::PrefixList": {
            "importProperties": [
                "PrefixListId"
            ]
        },
        "AWS::EC2::RouteTable": {
            "importProperties": [
                "RouteTableId"
            ]
        },
        "AWS::EC2::SecurityGroup": {
            "importProperties": [
                "GroupId"
            ]
        },
        "AWS::EC2::SpotFleet": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::Subnet": {
            "importProperties": [
                "SubnetId"
            ]
        },
        "AWS::EC2::SubnetRouteTableAssociation": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::TransitGateway": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::TransitGatewayConnect": {
            "importProperties": [
                "TransitGatewayAttachmentId"
            ]
        },
        "AWS::EC2::TransitGatewayMulticastDomain": {
            "importProperties": [
                "TransitGatewayMulticastDomainId"
            ]
        },
        "AWS::EC2::TransitGatewayMulticastDomainAssociation": {
            "importProperties": [
                "TransitGatewayMulticastDomainId",
                "TransitGatewayAttachmentId",
                "SubnetId"
            ]
        },
        "AWS::EC2::TransitGatewayMulticastGroupMember": {
            "importProperties": [
                "TransitGatewayMulticastDomainId",
                "GroupIpAddress",
                "NetworkInterfaceId"
            ]
        },
        "AWS::EC2::TransitGatewayMulticastGroupSource": {
            "importProperties": [
                "TransitGatewayMulticastDomainId",
                "GroupIpAddress",
                "NetworkInterfaceId"
            ]
        },
        "AWS::EC2::TransitGatewayPeeringAttachment": {
            "importProperties": [
                "TransitGatewayAttachmentId"
            ]
        },
        "AWS::EC2::TransitGatewayVpcAttachment": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EC2::VPC": {
            "importProperties": [
                "VpcId"
            ]
        },
        "AWS::EC2::VPCDHCPOptionsAssociation": {
            "importProperties": [
                "DhcpOptionsId",
                "VpcId"
            ]
        },
        "AWS::EC2::Volume": {
            "importProperties": [
                "VolumeId"
            ]
        },
        "AWS::ECR::PublicRepository": {
            "importProperties": [
                "RepositoryName"
            ]
        },
        "AWS::ECR::RegistryPolicy": {
            "importProperties": [
                "RegistryId"
            ]
        },
        "AWS::ECR::ReplicationConfiguration": {
            "importProperties": [
                "RegistryId"
            ]
        },
        "AWS::ECR::Repository": {
            "importProperties": [
                "RepositoryName"
            ]
        },
        "AWS::ECS::CapacityProvider": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::ECS::Cluster": {
            "importProperties": [
                "ClusterName"
            ]
        },
        "AWS::ECS::ClusterCapacityProviderAssociations": {
            "importProperties": [
                "Cluster"
            ]
        },
        "AWS::ECS::PrimaryTaskSet": {
            "importProperties": [
                "Cluster",
                "Service"
            ]
        },
        "AWS::ECS::Service": {
            "importProperties": [
                "ServiceArn",
                "Cluster"
            ]
        },
        "AWS::ECS::TaskDefinition": {
            "importProperties": [
                "TaskDefinitionArn"
            ]
        },
        "AWS::ECS::TaskSet": {
            "importProperties": [
                "Cluster",
                "Service",
                "Id"
            ]
        },
        "AWS::EFS::AccessPoint": {
            "importProperties": [
                "AccessPointId"
            ]
        },
        "AWS::EFS::FileSystem": {
            "importProperties": [
                "FileSystemId"
            ]
        },
        "AWS::EFS::MountTarget": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EKS::Addon": {
            "importProperties": [
                "ClusterName",
                "AddonName"
            ]
        },
        "AWS::EKS::Cluster": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::EKS::FargateProfile": {
            "importProperties": [
                "ClusterName",
                "FargateProfileName"
            ]
        },
        "AWS::EKS::Nodegroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::EMR::Studio": {
            "importProperties": [
                "StudioId"
            ]
        },
        "AWS::EMR::StudioSessionMapping": {
            "importProperties": [
                "StudioId",
                "IdentityType",
                "IdentityName"
            ]
        },
        "AWS::EMRContainers::VirtualCluster": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ElastiCache::GlobalReplicationGroup": {
            "importProperties": [
                "GlobalReplicationGroupId"
            ]
        },
        "AWS::ElastiCache::User": {
            "importProperties": [
                "UserId"
            ]
        },
        "AWS::ElastiCache::UserGroup": {
            "importProperties": [
                "UserGroupId"
            ]
        },
        "AWS::ElasticLoadBalancing::LoadBalancer": {
            "importProperties": [
                "LoadBalancerName"
            ]
        },
        "AWS::ElasticLoadBalancingV2::Listener": {
            "importProperties": [
                "ListenerArn"
            ]
        },
        "AWS::ElasticLoadBalancingV2::ListenerRule": {
            "importProperties": [
                "RuleArn"
            ]
        },
        "AWS::ElasticLoadBalancingV2::LoadBalancer": {
            "importProperties": [
                "LoadBalancerArn"
            ]
        },
        "AWS::EventSchemas::RegistryPolicy": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Events::ApiDestination": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Events::Archive": {
            "importProperties": [
                "ArchiveName"
            ]
        },
        "AWS::Events::Connection": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Events::Rule": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Evidently::Experiment": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Evidently::Feature": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Evidently::Launch": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Evidently::Project": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::FIS::ExperimentTemplate": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::FMS::NotificationChannel": {
            "importProperties": [
                "SnsTopicArn"
            ]
        },
        "AWS::FMS::Policy": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::FinSpace::Environment": {
            "importProperties": [
                "EnvironmentId"
            ]
        },
        "AWS::Forecast::Dataset": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Forecast::DatasetGroup": {
            "importProperties": [
                "DatasetGroupArn"
            ]
        },
        "AWS::FraudDetector::Detector": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::FraudDetector::EntityType": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::FraudDetector::EventType": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::FraudDetector::Label": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::FraudDetector::Outcome": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::FraudDetector::Variable": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::GameLift::Alias": {
            "importProperties": [
                "AliasId"
            ]
        },
        "AWS::GameLift::Fleet": {
            "importProperties": [
                "FleetId"
            ]
        },
        "AWS::GameLift::GameServerGroup": {
            "importProperties": [
                "GameServerGroupArn"
            ]
        },
        "AWS::GlobalAccelerator::Accelerator": {
            "importProperties": [
                "AcceleratorArn"
            ]
        },
        "AWS::GlobalAccelerator::EndpointGroup": {
            "importProperties": [
                "EndpointGroupArn"
            ]
        },
        "AWS::GlobalAccelerator::Listener": {
            "importProperties": [
                "ListenerArn"
            ]
        },
        "AWS::Glue::Registry": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Glue::Schema": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Glue::SchemaVersion": {
            "importProperties": [
                "VersionId"
            ]
        },
        "AWS::Glue::SchemaVersionMetadata": {
            "importProperties": [
                "SchemaVersionId",
                "Key",
                "Value"
            ]
        },
        "AWS::GreengrassV2::ComponentVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::GroundStation::Config": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::GroundStation::DataflowEndpointGroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::GroundStation::MissionProfile": {
            "importProperties": [
                "Id",
                "Arn"
            ]
        },
        "AWS::HealthLake::FHIRDatastore": {
            "importProperties": [
                "DatastoreId"
            ]
        },
        "AWS::IAM::Group": {
            "importProperties": [
                "GroupName"
            ],
            "capabilities": [
                "CAPABILITY_NAMED_IAM"
            ]
        },
        "AWS::IAM::InstanceProfile": {
            "importProperties": [
                "InstanceProfileName"
            ],
            "capabilities": [
                "CAPABILITY_NAMED_IAM"
            ]
        },
        "AWS::IAM::Role": {
            "importProperties": [
                "RoleName"
            ],
            "capabilities": [
                "CAPABILITY_NAMED_IAM"
            ]
        },
        "AWS::IAM::User": {
            "importProperties": [
                "UserName"
            ],
            "capabilities": [
                "CAPABILITY_NAMED_IAM"
            ]
        },
        "AWS::IAM::ManagedPolicy": {
            "importProperties": [
                "PolicyArn"
            ],
            "capabilities": [
                "CAPABILITY_NAMED_IAM"
            ]
        },
        "AWS::IAM::OIDCProvider": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IAM::SAMLProvider": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IAM::ServerCertificate": {
            "importProperties": [
                "ServerCertificateName"
            ]
        },
        "AWS::IAM::VirtualMFADevice": {
            "importProperties": [
                "SerialNumber"
            ]
        },
        "AWS::IVS::Channel": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IVS::PlaybackKeyPair": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IVS::RecordingConfiguration": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IVS::StreamKey": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::Component": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::ContainerRecipe": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::DistributionConfiguration": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::Image": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::ImagePipeline": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::ImageRecipe": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::ImageBuilder::InfrastructureConfiguration": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Inspector::AssessmentTarget": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Inspector::AssessmentTemplate": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Inspector::ResourceGroup": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::InspectorV2::Filter": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IoT::AccountAuditConfiguration": {
            "importProperties": [
                "AccountId"
            ]
        },
        "AWS::IoT::Authorizer": {
            "importProperties": [
                "AuthorizerName"
            ]
        },
        "AWS::IoT::Certificate": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoT::CustomMetric": {
            "importProperties": [
                "MetricName"
            ]
        },
        "AWS::IoT::Dimension": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::IoT::DomainConfiguration": {
            "importProperties": [
                "DomainConfigurationName"
            ]
        },
        "AWS::IoT::FleetMetric": {
            "importProperties": [
                "MetricName"
            ]
        },
        "AWS::IoT::JobTemplate": {
            "importProperties": [
                "JobTemplateId"
            ]
        },
        "AWS::IoT::Logging": {
            "importProperties": [
                "AccountId"
            ]
        },
        "AWS::IoT::MitigationAction": {
            "importProperties": [
                "ActionName"
            ]
        },
        "AWS::IoT::ProvisioningTemplate": {
            "importProperties": [
                "TemplateName"
            ]
        },
        "AWS::IoT::ResourceSpecificLogging": {
            "importProperties": [
                "TargetId"
            ]
        },
        "AWS::IoT::ScheduledAudit": {
            "importProperties": [
                "ScheduledAuditName"
            ]
        },
        "AWS::IoT::SecurityProfile": {
            "importProperties": [
                "SecurityProfileName"
            ]
        },
        "AWS::IoT::Thing": {
            "importProperties": [
                "ThingName"
            ]
        },
        "AWS::IoT::TopicRule": {
            "importProperties": [
                "RuleName"
            ]
        },
        "AWS::IoT::TopicRuleDestination": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::IoTAnalytics::Channel": {
            "importProperties": [
                "ChannelName"
            ]
        },
        "AWS::IoTAnalytics::Dataset": {
            "importProperties": [
                "DatasetName"
            ]
        },
        "AWS::IoTAnalytics::Datastore": {
            "importProperties": [
                "DatastoreName"
            ]
        },
        "AWS::IoTAnalytics::Pipeline": {
            "importProperties": [
                "PipelineName"
            ]
        },
        "AWS::IoTCoreDeviceAdvisor::SuiteDefinition": {
            "importProperties": [
                "SuiteDefinitionId"
            ]
        },
        "AWS::IoTEvents::DetectorModel": {
            "importProperties": [
                "DetectorModelName"
            ]
        },
        "AWS::IoTEvents::Input": {
            "importProperties": [
                "InputName"
            ]
        },
        "AWS::IoTFleetHub::Application": {
            "importProperties": [
                "ApplicationId"
            ]
        },
        "AWS::IoTSiteWise::AccessPolicy": {
            "importProperties": [
                "AccessPolicyId"
            ]
        },
        "AWS::IoTSiteWise::Asset": {
            "importProperties": [
                "AssetId"
            ]
        },
        "AWS::IoTSiteWise::AssetModel": {
            "importProperties": [
                "AssetModelId"
            ]
        },
        "AWS::IoTSiteWise::Dashboard": {
            "importProperties": [
                "DashboardId"
            ]
        },
        "AWS::IoTSiteWise::Gateway": {
            "importProperties": [
                "GatewayId"
            ]
        },
        "AWS::IoTSiteWise::Portal": {
            "importProperties": [
                "PortalId"
            ]
        },
        "AWS::IoTSiteWise::Project": {
            "importProperties": [
                "ProjectId"
            ]
        },
        "AWS::IoTWireless::Destination": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::IoTWireless::DeviceProfile": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoTWireless::FuotaTask": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoTWireless::MulticastGroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoTWireless::PartnerAccount": {
            "importProperties": [
                "PartnerAccountId"
            ]
        },
        "AWS::IoTWireless::ServiceProfile": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoTWireless::TaskDefinition": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoTWireless::WirelessDevice": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::IoTWireless::WirelessGateway": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::KMS::Alias": {
            "importProperties": [
                "AliasName"
            ]
        },
        "AWS::KMS::Key": {
            "importProperties": [
                "KeyId"
            ]
        },
        "AWS::KMS::ReplicaKey": {
            "importProperties": [
                "KeyId"
            ]
        },
        "AWS::KafkaConnect::Connector": {
            "importProperties": [
                "ConnectorArn"
            ]
        },
        "AWS::Kendra::DataSource": {
            "importProperties": [
                "Id",
                "IndexId"
            ]
        },
        "AWS::Kendra::Faq": {
            "importProperties": [
                "Id",
                "IndexId"
            ]
        },
        "AWS::Kendra::Index": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Kinesis::Stream": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::KinesisFirehose::DeliveryStream": {
            "importProperties": [
                "DeliveryStreamName"
            ]
        },
        "AWS::KinesisVideo::SignalingChannel": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::KinesisVideo::Stream": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Lambda::Alias": {
            "importProperties": [
                "AliasArn"
            ]
        },
        "AWS::Lambda::CodeSigningConfig": {
            "importProperties": [
                "CodeSigningConfigArn"
            ]
        },
        "AWS::Lambda::EventSourceMapping": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Lambda::Function": {
            "importProperties": [
                "FunctionName"
            ]
        },
        "AWS::Lambda::Version": {
            "importProperties": [
                "FunctionArn"
            ]
        },
        "AWS::Lex::Bot": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Lex::BotAlias": {
            "importProperties": [
                "BotAliasId",
                "BotId"
            ]
        },
        "AWS::Lex::BotVersion": {
            "importProperties": [
                "BotId",
                "BotVersion"
            ]
        },
        "AWS::Lex::ResourcePolicy": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::LicenseManager::Grant": {
            "importProperties": [
                "GrantArn"
            ]
        },
        "AWS::LicenseManager::License": {
            "importProperties": [
                "LicenseArn"
            ]
        },
        "AWS::Lightsail::Alarm": {
            "importProperties": [
                "AlarmName"
            ]
        },
        "AWS::Lightsail::Bucket": {
            "importProperties": [
                "BucketName"
            ]
        },
        "AWS::Lightsail::Certificate": {
            "importProperties": [
                "CertificateName"
            ]
        },
        "AWS::Lightsail::Container": {
            "importProperties": [
                "ServiceName"
            ]
        },
        "AWS::Lightsail::Database": {
            "importProperties": [
                "RelationalDatabaseName"
            ]
        },
        "AWS::Lightsail::Disk": {
            "importProperties": [
                "DiskName"
            ]
        },
        "AWS::Lightsail::Distribution": {
            "importProperties": [
                "DistributionName"
            ]
        },
        "AWS::Lightsail::Instance": {
            "importProperties": [
                "InstanceName"
            ]
        },
        "AWS::Lightsail::LoadBalancer": {
            "importProperties": [
                "LoadBalancerName"
            ]
        },
        "AWS::Lightsail::LoadBalancerTlsCertificate": {
            "importProperties": [
                "CertificateName",
                "LoadBalancerName"
            ]
        },
        "AWS::Lightsail::StaticIp": {
            "importProperties": [
                "StaticIpName"
            ]
        },
        "AWS::Location::GeofenceCollection": {
            "importProperties": [
                "CollectionName"
            ]
        },
        "AWS::Location::Map": {
            "importProperties": [
                "MapName"
            ]
        },
        "AWS::Location::PlaceIndex": {
            "importProperties": [
                "IndexName"
            ]
        },
        "AWS::Location::RouteCalculator": {
            "importProperties": [
                "CalculatorName"
            ]
        },
        "AWS::Location::Tracker": {
            "importProperties": [
                "TrackerName"
            ]
        },
        "AWS::Location::TrackerConsumer": {
            "importProperties": [
                "TrackerName",
                "ConsumerArn"
            ]
        },
        "AWS::Logs::LogGroup": {
            "importProperties": [
                "LogGroupName"
            ]
        },
        "AWS::Logs::MetricFilter": {
            "importProperties": [
                "FilterName"
            ]
        },
        "AWS::Logs::QueryDefinition": {
            "importProperties": [
                "QueryDefinitionId"
            ]
        },
        "AWS::Logs::ResourcePolicy": {
            "importProperties": [
                "PolicyName"
            ]
        },
        "AWS::Logs::SubscriptionFilter": {
            "importProperties": [
                "FilterName"
            ]
        },
        "AWS::LookoutEquipment::InferenceScheduler": {
            "importProperties": [
                "InferenceSchedulerName"
            ]
        },
        "AWS::LookoutMetrics::Alert": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::LookoutMetrics::AnomalyDetector": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::LookoutVision::Project": {
            "importProperties": [
                "ProjectName"
            ]
        },
        "AWS::MSK::Cluster": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::MWAA::Environment": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Macie::CustomDataIdentifier": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Macie::FindingsFilter": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Macie::Session": {
            "importProperties": [
                "AwsAccountId"
            ]
        },
        "AWS::MediaConnect::Flow": {
            "importProperties": [
                "FlowArn"
            ]
        },
        "AWS::MediaConnect::FlowEntitlement": {
            "importProperties": [
                "EntitlementArn"
            ]
        },
        "AWS::MediaConnect::FlowOutput": {
            "importProperties": [
                "OutputArn"
            ]
        },
        "AWS::MediaConnect::FlowSource": {
            "importProperties": [
                "SourceArn"
            ]
        },
        "AWS::MediaConnect::FlowVpcInterface": {
            "importProperties": [
                "FlowArn",
                "Name"
            ]
        },
        "AWS::MediaPackage::Asset": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::MediaPackage::Channel": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::MediaPackage::OriginEndpoint": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::MediaPackage::PackagingConfiguration": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::MediaPackage::PackagingGroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::MemoryDB::ACL": {
            "importProperties": [
                "ACLName"
            ]
        },
        "AWS::MemoryDB::Cluster": {
            "importProperties": [
                "ClusterName"
            ]
        },
        "AWS::MemoryDB::ParameterGroup": {
            "importProperties": [
                "ParameterGroupName"
            ]
        },
        "AWS::MemoryDB::SubnetGroup": {
            "importProperties": [
                "SubnetGroupName"
            ]
        },
        "AWS::MemoryDB::User": {
            "importProperties": [
                "UserName"
            ]
        },
        "AWS::NetworkFirewall::Firewall": {
            "importProperties": [
                "FirewallArn"
            ]
        },
        "AWS::NetworkFirewall::FirewallPolicy": {
            "importProperties": [
                "FirewallPolicyArn"
            ]
        },
        "AWS::NetworkFirewall::LoggingConfiguration": {
            "importProperties": [
                "FirewallArn"
            ]
        },
        "AWS::NetworkFirewall::RuleGroup": {
            "importProperties": [
                "RuleGroupArn"
            ]
        },
        "AWS::NetworkManager::CustomerGatewayAssociation": {
            "importProperties": [
                "GlobalNetworkId",
                "CustomerGatewayArn"
            ]
        },
        "AWS::NetworkManager::Device": {
            "importProperties": [
                "GlobalNetworkId",
                "DeviceId"
            ]
        },
        "AWS::NetworkManager::GlobalNetwork": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::NetworkManager::Link": {
            "importProperties": [
                "GlobalNetworkId",
                "LinkId"
            ]
        },
        "AWS::NetworkManager::LinkAssociation": {
            "importProperties": [
                "GlobalNetworkId",
                "DeviceId",
                "LinkId"
            ]
        },
        "AWS::NetworkManager::Site": {
            "importProperties": [
                "GlobalNetworkId",
                "SiteId"
            ]
        },
        "AWS::NetworkManager::TransitGatewayRegistration": {
            "importProperties": [
                "GlobalNetworkId",
                "TransitGatewayArn"
            ]
        },
        "AWS::NimbleStudio::LaunchProfile": {
            "importProperties": [
                "LaunchProfileId",
                "StudioId"
            ]
        },
        "AWS::NimbleStudio::StreamingImage": {
            "importProperties": [
                "StudioId",
                "StreamingImageId"
            ]
        },
        "AWS::NimbleStudio::Studio": {
            "importProperties": [
                "StudioId"
            ]
        },
        "AWS::NimbleStudio::StudioComponent": {
            "importProperties": [
                "StudioComponentId",
                "StudioId"
            ]
        },
        "AWS::OpenSearchService::Domain": {
            "importProperties": [
                "DomainName"
            ]
        },
        "AWS::OpsWorksCM::Server": {
            "importProperties": [
                "ServerName"
            ]
        },
        "AWS::Panorama::ApplicationInstance": {
            "importProperties": [
                "ApplicationInstanceId"
            ]
        },
        "AWS::Panorama::Package": {
            "importProperties": [
                "PackageId"
            ]
        },
        "AWS::Panorama::PackageVersion": {
            "importProperties": [
                "PackageId",
                "PackageVersion",
                "PatchVersion"
            ]
        },
        "AWS::Pinpoint::InAppTemplate": {
            "importProperties": [
                "TemplateName"
            ]
        },
        "AWS::QLDB::Stream": {
            "importProperties": [
                "LedgerName",
                "Id"
            ]
        },
        "AWS::QuickSight::Analysis": {
            "importProperties": [
                "AnalysisId",
                "AwsAccountId"
            ]
        },
        "AWS::QuickSight::Dashboard": {
            "importProperties": [
                "AwsAccountId",
                "DashboardId"
            ]
        },
        "AWS::QuickSight::DataSet": {
            "importProperties": [
                "AwsAccountId",
                "DataSetId"
            ]
        },
        "AWS::QuickSight::DataSource": {
            "importProperties": [
                "AwsAccountId",
                "DataSourceId"
            ]
        },
        "AWS::QuickSight::Template": {
            "importProperties": [
                "AwsAccountId",
                "TemplateId"
            ]
        },
        "AWS::QuickSight::Theme": {
            "importProperties": [
                "ThemeId",
                "AwsAccountId"
            ]
        },
        "AWS::RDS::DBCluster": {
            "importProperties": [
                "DBClusterIdentifier"
            ]
        },
        "AWS::RDS::DBInstance": {
            "importProperties": [
                "DBInstanceIdentifier"
            ]
        },
        "AWS::RDS::DBProxy": {
            "importProperties": [
                "DBProxyName"
            ]
        },
        "AWS::RDS::DBProxyEndpoint": {
            "importProperties": [
                "DBProxyEndpointName"
            ]
        },
        "AWS::RDS::DBProxyTargetGroup": {
            "importProperties": [
                "TargetGroupArn"
            ]
        },
        "AWS::RDS::GlobalCluster": {
            "importProperties": [
                "GlobalClusterIdentifier"
            ]
        },
        "AWS::RUM::AppMonitor": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Redshift::Cluster": {
            "importProperties": [
                "ClusterIdentifier"
            ]
        },
        "AWS::Redshift::EndpointAccess": {
            "importProperties": [
                "EndpointName"
            ]
        },
        "AWS::Redshift::EndpointAuthorization": {
            "importProperties": [
                "ClusterIdentifier",
                "Account"
            ]
        },
        "AWS::Redshift::EventSubscription": {
            "importProperties": [
                "SubscriptionName"
            ]
        },
        "AWS::Redshift::ScheduledAction": {
            "importProperties": [
                "ScheduledActionName"
            ]
        },
        "AWS::RefactorSpaces::Application": {
            "importProperties": [
                "EnvironmentIdentifier",
                "ApplicationIdentifier"
            ]
        },
        "AWS::RefactorSpaces::Environment": {
            "importProperties": [
                "EnvironmentIdentifier"
            ]
        },
        "AWS::RefactorSpaces::Route": {
            "importProperties": [
                "EnvironmentIdentifier",
                "ApplicationIdentifier",
                "RouteIdentifier"
            ]
        },
        "AWS::RefactorSpaces::Service": {
            "importProperties": [
                "EnvironmentIdentifier",
                "ApplicationIdentifier",
                "ServiceIdentifier"
            ]
        },
        "AWS::Rekognition::Collection": {
            "importProperties": [
                "CollectionId"
            ]
        },
        "AWS::Rekognition::Project": {
            "importProperties": [
                "ProjectName"
            ]
        },
        "AWS::ResilienceHub::App": {
            "importProperties": [
                "AppArn"
            ]
        },
        "AWS::ResilienceHub::ResiliencyPolicy": {
            "importProperties": [
                "PolicyArn"
            ]
        },
        "AWS::ResourceGroups::Group": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::RoboMaker::Fleet": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::RoboMaker::Robot": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::RoboMaker::RobotApplication": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::RoboMaker::RobotApplicationVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::RoboMaker::SimulationApplication": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::RoboMaker::SimulationApplicationVersion": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Route53::DNSSEC": {
            "importProperties": [
                "HostedZoneId"
            ]
        },
        "AWS::Route53::HealthCheck": {
            "importProperties": [
                "HealthCheckId"
            ]
        },
        "AWS::Route53::HostedZone": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53::KeySigningKey": {
            "importProperties": [
                "HostedZoneId",
                "Name"
            ]
        },
        "AWS::Route53RecoveryControl::Cluster": {
            "importProperties": [
                "ClusterArn"
            ]
        },
        "AWS::Route53RecoveryControl::ControlPanel": {
            "importProperties": [
                "ControlPanelArn"
            ]
        },
        "AWS::Route53RecoveryControl::RoutingControl": {
            "importProperties": [
                "RoutingControlArn"
            ]
        },
        "AWS::Route53RecoveryControl::SafetyRule": {
            "importProperties": [
                "SafetyRuleArn"
            ]
        },
        "AWS::Route53RecoveryReadiness::Cell": {
            "importProperties": [
                "CellName"
            ]
        },
        "AWS::Route53RecoveryReadiness::ReadinessCheck": {
            "importProperties": [
                "ReadinessCheckName"
            ]
        },
        "AWS::Route53RecoveryReadiness::RecoveryGroup": {
            "importProperties": [
                "RecoveryGroupName"
            ]
        },
        "AWS::Route53RecoveryReadiness::ResourceSet": {
            "importProperties": [
                "ResourceSetName"
            ]
        },
        "AWS::Route53Resolver::FirewallDomainList": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::FirewallRuleGroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::FirewallRuleGroupAssociation": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::ResolverConfig": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::ResolverDNSSECConfig": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::ResolverQueryLoggingConfig": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Route53Resolver::ResolverRule": {
            "importProperties": [
                "ResolverRuleId"
            ]
        },
        "AWS::Route53Resolver::ResolverRuleAssociation": {
            "importProperties": [
                "ResolverRuleAssociationId"
            ]
        },
        "AWS::S3::AccessPoint": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::S3::Bucket": {
            "importProperties": [
                "BucketName"
            ]
        },
        "AWS::S3::MultiRegionAccessPoint": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::S3::MultiRegionAccessPointPolicy": {
            "importProperties": [
                "MrapName"
            ]
        },
        "AWS::S3ObjectLambda::AccessPoint": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::S3ObjectLambda::AccessPointPolicy": {
            "importProperties": [
                "ObjectLambdaAccessPoint"
            ]
        },
        "AWS::S3Outposts::AccessPoint": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::S3Outposts::Bucket": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::S3Outposts::BucketPolicy": {
            "importProperties": [
                "Bucket"
            ]
        },
        "AWS::S3Outposts::Endpoint": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::SES::ConfigurationSet": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::SES::ConfigurationSetEventDestination": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::SES::ContactList": {
            "importProperties": [
                "ContactListName"
            ]
        },
        "AWS::SES::Template": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::SNS::Topic": {
            "importProperties": [
                "TopicArn"
            ]
        },
        "AWS::SQS::Queue": {
            "importProperties": [
                "QueueUrl"
            ]
        },
        "AWS::SSM::Association": {
            "importProperties": [
                "AssociationId"
            ]
        },
        "AWS::SSM::Document": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::SSM::ResourceDataSync": {
            "importProperties": [
                "SyncName"
            ]
        },
        "AWS::SSMContacts::Contact": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::SSMContacts::ContactChannel": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::SSMIncidents::ReplicationSet": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::SSMIncidents::ResponsePlan": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::SSO::InstanceAccessControlAttributeConfiguration": {
            "importProperties": [
                "InstanceArn"
            ]
        },
        "AWS::SSO::PermissionSet": {
            "importProperties": [
                "InstanceArn",
                "PermissionSetArn"
            ]
        },
        "AWS::SageMaker::App": {
            "importProperties": [
                "AppName",
                "AppType",
                "DomainId",
                "UserProfileName"
            ]
        },
        "AWS::SageMaker::AppImageConfig": {
            "importProperties": [
                "AppImageConfigName"
            ]
        },
        "AWS::SageMaker::DataQualityJobDefinition": {
            "importProperties": [
                "JobDefinitionArn"
            ]
        },
        "AWS::SageMaker::Device": {
            "importProperties": [
                "DeviceFleetName"
            ]
        },
        "AWS::SageMaker::DeviceFleet": {
            "importProperties": [
                "DeviceFleetName"
            ]
        },
        "AWS::SageMaker::Domain": {
            "importProperties": [
                "DomainId"
            ]
        },
        "AWS::SageMaker::FeatureGroup": {
            "importProperties": [
                "FeatureGroupName"
            ]
        },
        "AWS::SageMaker::Image": {
            "importProperties": [
                "ImageArn"
            ]
        },
        "AWS::SageMaker::ImageVersion": {
            "importProperties": [
                "ImageVersionArn"
            ]
        },
        "AWS::SageMaker::ModelBiasJobDefinition": {
            "importProperties": [
                "JobDefinitionArn"
            ]
        },
        "AWS::SageMaker::ModelExplainabilityJobDefinition": {
            "importProperties": [
                "JobDefinitionArn"
            ]
        },
        "AWS::SageMaker::ModelPackageGroup": {
            "importProperties": [
                "ModelPackageGroupArn"
            ]
        },
        "AWS::SageMaker::ModelQualityJobDefinition": {
            "importProperties": [
                "JobDefinitionArn"
            ]
        },
        "AWS::SageMaker::MonitoringSchedule": {
            "importProperties": [
                "MonitoringScheduleArn"
            ]
        },
        "AWS::SageMaker::Pipeline": {
            "importProperties": [
                "PipelineName"
            ]
        },
        "AWS::SageMaker::Project": {
            "importProperties": [
                "ProjectArn"
            ]
        },
        "AWS::SageMaker::UserProfile": {
            "importProperties": [
                "UserProfileName",
                "DomainId"
            ]
        },
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct": {
            "importProperties": [
                "ProvisionedProductId"
            ]
        },
        "AWS::ServiceCatalog::ServiceAction": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ServiceCatalog::ServiceActionAssociation": {
            "importProperties": [
                "ProductId",
                "ProvisioningArtifactId",
                "ServiceActionId"
            ]
        },
        "AWS::ServiceCatalogAppRegistry::Application": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ServiceCatalogAppRegistry::AttributeGroup": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::ServiceCatalogAppRegistry::ResourceAssociation": {
            "importProperties": [
                "Id"
            ]
        },
        "AWS::Signer::ProfilePermission": {
            "importProperties": [
                "StatementId",
                "ProfileName"
            ]
        },
        "AWS::Signer::SigningProfile": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::StepFunctions::Activity": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::StepFunctions::StateMachine": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Synthetics::Canary": {
            "importProperties": [
                "Name"
            ]
        },
        "AWS::Timestream::Database": {
            "importProperties": [
                "DatabaseName"
            ]
        },
        "AWS::Timestream::ScheduledQuery": {
            "importProperties": [
                "Arn"
            ]
        },
        "AWS::Timestream::Table": {
            "importProperties": [
                "DatabaseName",
                "TableName"
            ]
        },
        "AWS::Transfer::Workflow": {
            "importProperties": [
                "WorkflowId"
            ]
        },
        "AWS::WAFv2::IPSet": {
            "importProperties": [
                "Name",
                "Id",
                "Scope"
            ]
        },
        "AWS::WAFv2::LoggingConfiguration": {
            "importProperties": [
                "ResourceArn"
            ]
        },
        "AWS::WAFv2::RegexPatternSet": {
            "importProperties": [
                "Name",
                "Id",
                "Scope"
            ]
        },
        "AWS::WAFv2::RuleGroup": {
            "importProperties": [
                "Name",
                "Id",
                "Scope"
            ]
        },
        "AWS::WAFv2::WebACL": {
            "importProperties": [
                "Name",
                "Id",
                "Scope"
            ]
        },
        "AWS::WAFv2::WebACLAssociation": {
            "importProperties": [
                "ResourceArn",
                "WebACLArn"
            ]
        },
        "AWS::Wisdom::Assistant": {
            "importProperties": [
                "AssistantId"
            ]
        },
        "AWS::Wisdom::AssistantAssociation": {
            "importProperties": [
                "AssistantAssociationId",
                "AssistantId"
            ]
        },
        "AWS::Wisdom::KnowledgeBase": {
            "importProperties": [
                "KnowledgeBaseId"
            ]
        },
        "AWS::WorkSpaces::ConnectionAlias": {
            "importProperties": [
                "AliasId"
            ]
        },
        "AWS::XRay::Group": {
            "importProperties": [
                "GroupARN"
            ]
        },
        "AWS::XRay::SamplingRule": {
            "importProperties": [
                "RuleARN"
            ]
        }
    }
