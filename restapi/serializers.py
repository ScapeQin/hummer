from rest_framework import serializers

from backend.models import (MyUser, Project, Image, Application, AutoScaler,
    Environment, Port, ResourceLimit, Volume)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('url', 'id', 'username', 'email', 'is_staff', 'is_active')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'id', 'name', 'desc', 'create_time', 'members')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'user', 'project', 'name', 'desc', 'version', 'digest',
            'token', 'is_public', 'create_time', 'status')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'user', 'image', 'name', 'replicas', 'resource_limit',
            'session_affinity', 'internal_ip', 'external_ip', 'is_autoscaler',
            'create_time','status')


class AutoScalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoScaler
        fields = ('id', 'app', 'min_replicas', 'max_replicas', 'cpu_target')


class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('id', 'app', 'name', 'protocol', 'internal_port',
            'external_port')


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ('id', 'app', 'name', 'value')


class ResourceLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceLimit
        fields = ('id', 'name', 'cpu', 'cpu_unit', 'memory', 'memory_unit')


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('id', 'user', 'project', 'app', 'mount_path', 'name', 'desc',
            'capacity', 'capacity_unit', 'status', 'create_time')
