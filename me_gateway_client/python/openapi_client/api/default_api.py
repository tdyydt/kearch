# coding: utf-8

"""
    Kearch meta search engine gateway API

    Kearch meta search engine gateway API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_a_conenction_request_post(self, connection_request_on_me, **kwargs):  # noqa: E501
        """Add a connection request sent from specialist server to meta server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_a_conenction_request_post(connection_request_on_me, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectionRequestOnME connection_request_on_me: A connection request. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_a_conenction_request_post_with_http_info(connection_request_on_me, **kwargs)  # noqa: E501
        else:
            (data) = self.add_a_conenction_request_post_with_http_info(connection_request_on_me, **kwargs)  # noqa: E501
            return data

    def add_a_conenction_request_post_with_http_info(self, connection_request_on_me, **kwargs):  # noqa: E501
        """Add a connection request sent from specialist server to meta server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_a_conenction_request_post_with_http_info(connection_request_on_me, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectionRequestOnME connection_request_on_me: A connection request. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['connection_request_on_me']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_a_conenction_request_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'connection_request_on_me' is set
        if ('connection_request_on_me' not in local_var_params or
                local_var_params['connection_request_on_me'] is None):
            raise ValueError("Missing the required parameter `connection_request_on_me` when calling `add_a_conenction_request_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'connection_request_on_me' in local_var_params:
            body_params = local_var_params['connection_request_on_me']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/add_a_conenction_request', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_a_summary_post(self, summary, **kwargs):  # noqa: E501
        """Add a summary to meta server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_a_summary_post(summary, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Summary summary: A summary of the specialist server. (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_a_summary_post_with_http_info(summary, **kwargs)  # noqa: E501
        else:
            (data) = self.add_a_summary_post_with_http_info(summary, **kwargs)  # noqa: E501
            return data

    def add_a_summary_post_with_http_info(self, summary, **kwargs):  # noqa: E501
        """Add a summary to meta server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_a_summary_post_with_http_info(summary, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Summary summary: A summary of the specialist server. (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['summary']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_a_summary_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'summary' is set
        if ('summary' not in local_var_params or
                local_var_params['summary'] is None):
            raise ValueError("Missing the required parameter `summary` when calling `add_a_summary_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'summary' in local_var_params:
            body_params = local_var_params['summary']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/add_a_summary', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_a_conenction_request_delete(self, **kwargs):  # noqa: E501
        """Delete a connection request sent from specialist server to this meta server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_a_conenction_request_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sp_host: A specialist host name of the connection request to delete.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_a_conenction_request_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_a_conenction_request_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_a_conenction_request_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Delete a connection request sent from specialist server to this meta server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_a_conenction_request_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sp_host: A specialist host name of the connection request to delete.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['sp_host']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_a_conenction_request_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sp_host' in local_var_params:
            query_params.append(('sp_host', local_var_params['sp_host']))  # noqa: E501

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
            '/delete_a_conenction_request', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_get(self, **kwargs):  # noqa: E501
        """Retrieve search results.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queries: Space-separated query words
        :param int max_urls: Max number of URLs to retrive from specialist servers
        :param str sp_host: A host name to retrieve results from.
        :return: list[Document]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve search results.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queries: Space-separated query words
        :param int max_urls: Max number of URLs to retrive from specialist servers
        :param str sp_host: A host name to retrieve results from.
        :return: list[Document]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['queries', 'max_urls', 'sp_host']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'queries' in local_var_params:
            query_params.append(('queries', local_var_params['queries']))  # noqa: E501
        if 'max_urls' in local_var_params:
            query_params.append(('max_urls', local_var_params['max_urls']))  # noqa: E501
        if 'sp_host' in local_var_params:
            query_params.append(('sp_host', local_var_params['sp_host']))  # noqa: E501

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
            '/retrieve', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Document]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
