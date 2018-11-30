# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.3
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kba.api_client import ApiClient


class MetadataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_beacons(self, **kwargs):  # noqa: E501
        """get_beacons  # noqa: E501

        Get a list of all of the knowledge beacons that the aggregator can query   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_beacons(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[ServerKnowledgeBeacon]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_beacons_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_beacons_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_beacons_with_http_info(self, **kwargs):  # noqa: E501
        """get_beacons  # noqa: E501

        Get a list of all of the knowledge beacons that the aggregator can query   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_beacons_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[ServerKnowledgeBeacon]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_beacons" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/beacons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServerKnowledgeBeacon]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_concept_categories(self, **kwargs):  # noqa: E501
        """get_concept_categories  # noqa: E501

        Get a list of semantic categories and number of instances in each available knowledge beacon, including associated beacon-specific metadata   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_concept_categories(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[int] beacons: set of aggregator indices of beacons to constrain categories returned 
        :return: list[ServerConceptCategory]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_concept_categories_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_concept_categories_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_concept_categories_with_http_info(self, **kwargs):  # noqa: E501
        """get_concept_categories  # noqa: E501

        Get a list of semantic categories and number of instances in each available knowledge beacon, including associated beacon-specific metadata   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_concept_categories_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[int] beacons: set of aggregator indices of beacons to constrain categories returned 
        :return: list[ServerConceptCategory]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['beacons']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_concept_categories" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'beacons' in params:
            query_params.append(('beacons', params['beacons']))  # noqa: E501
            collection_formats['beacons'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServerConceptCategory]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_error_log(self, query_id, **kwargs):  # noqa: E501
        """get_error_log  # noqa: E501

        Get a log of the system errors associated with a specified query   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_error_log(query_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query_id: query identifier returned from a POSTed query  (required)
        :return: list[ServerLogEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_error_log_with_http_info(query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_error_log_with_http_info(query_id, **kwargs)  # noqa: E501
            return data

    def get_error_log_with_http_info(self, query_id, **kwargs):  # noqa: E501
        """get_error_log  # noqa: E501

        Get a log of the system errors associated with a specified query   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_error_log_with_http_info(query_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str query_id: query identifier returned from a POSTed query  (required)
        :return: list[ServerLogEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_error_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params or
                params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `get_error_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_id' in params:
            query_params.append(('queryId', params['query_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/errorlog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServerLogEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_knowledge_map(self, **kwargs):  # noqa: E501
        """get_knowledge_map  # noqa: E501

        Get a high level knowledge map of the all the beacons specified by triplets of subject concept category, relationship predicate and concept object category   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_knowledge_map(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[int] beacons: set of aggregator indices of beacons constraining knowledge maps returned 
        :return: list[ServerKnowledgeMap]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_knowledge_map_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_knowledge_map_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_knowledge_map_with_http_info(self, **kwargs):  # noqa: E501
        """get_knowledge_map  # noqa: E501

        Get a high level knowledge map of the all the beacons specified by triplets of subject concept category, relationship predicate and concept object category   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_knowledge_map_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[int] beacons: set of aggregator indices of beacons constraining knowledge maps returned 
        :return: list[ServerKnowledgeMap]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['beacons']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_map" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'beacons' in params:
            query_params.append(('beacons', params['beacons']))  # noqa: E501
            collection_formats['beacons'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/kmap', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServerKnowledgeMap]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_predicates(self, **kwargs):  # noqa: E501
        """get_predicates  # noqa: E501

        Get a list of predicates used in statements issued by the knowledge source   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_predicates(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[int] beacons: set of aggregator indices of beacons to constrain predicates returned 
        :return: list[ServerPredicate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_predicates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_predicates_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_predicates_with_http_info(self, **kwargs):  # noqa: E501
        """get_predicates  # noqa: E501

        Get a list of predicates used in statements issued by the knowledge source   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_predicates_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[int] beacons: set of aggregator indices of beacons to constrain predicates returned 
        :return: list[ServerPredicate]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['beacons']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_predicates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'beacons' in params:
            query_params.append(('beacons', params['beacons']))  # noqa: E501
            collection_formats['beacons'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/predicates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServerPredicate]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
